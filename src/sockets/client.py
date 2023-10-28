from socket import socket, AF_INET, SOCK_STREAM, error
from threading import Thread
from json import dumps, loads
from typing import Callable


PORT: int | None = None
TARGET_PORT: int | None = None
HOST = None
client: socket | None = None

RECEIVE_MESSAGE_DELEGATE_TARGET: Callable[[str], None] | None = None
RECEIVE_MESSAGE_DELEGATE_CLIENT: Callable[[str], None] | None = None


def receive() -> None:
    while True:
        try:
            message = client.recv(1024)
            message_dict = loads(message.decode('utf-8'))
            if message_dict['target_port'] == PORT:
                RECEIVE_MESSAGE_DELEGATE_TARGET(message_dict['message'])
            else:
                RECEIVE_MESSAGE_DELEGATE_CLIENT(message_dict['message'])
        except error:
            client.close()
            break


def send(message: str) -> None:
    message_dict = {
        'sender_port': PORT,
        'target_port': TARGET_PORT,
        'message': message
    }
    message = dumps(message_dict)

    client.send(message.encode('utf-8'))


def start(receive_message_delegate_target: Callable[[str], None],
          receive_message_delegate_client: Callable[[str], None]) -> None:
    global PORT, TARGET_PORT, HOST, client, RECEIVE_MESSAGE_DELEGATE_TARGET, RECEIVE_MESSAGE_DELEGATE_CLIENT

    RECEIVE_MESSAGE_DELEGATE_TARGET = receive_message_delegate_target
    RECEIVE_MESSAGE_DELEGATE_CLIENT = receive_message_delegate_client

    PORT = int(input('Enter the port: '))
    TARGET_PORT = int(input('Enter the target port: '))
    HOST = '127.0.0.1'

    client = socket(AF_INET, SOCK_STREAM)
    client.bind((HOST, PORT))
    client.connect((HOST, 5000))

    thread_receive = Thread(target=receive)
    thread_receive.start()
