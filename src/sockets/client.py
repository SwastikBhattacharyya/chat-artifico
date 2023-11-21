from socket import socket, AF_INET, SOCK_STREAM, error
from json import dumps, loads
from typing import Callable
from src.database.database_client import DatabaseClient
from src.data.data import Data
from threading import Thread


PORT: int | None = None
TARGET_PORT: int | None = None
HOST = None
client: socket | None = None
running: bool = True

RECEIVE_MESSAGE_DELEGATE_TARGET: Callable[[str], None] | None = None
RECEIVE_MESSAGE_DELEGATE_CLIENT: Callable[[str], None] | None = None
USER_NOT_SELECTED_MESSAGE_DELEGATE: Callable[[], None] | None = None
GET_SELECTED_USER_NAME: Callable[[], str] | None = None


def set_port(port: int) -> None:
    global PORT
    PORT = port


def get_port() -> int:
    global PORT
    return PORT


def set_target_port(target_port: int) -> None:
    global TARGET_PORT
    TARGET_PORT = target_port


def handle_message(message_dict: dict) -> None:
    if message_dict['target_port'] == PORT:
        username = DatabaseClient.users_collection.find_one({'port': message_dict['sender_port']})['user_name']
        if username not in Data.chats:
            Data.chats[username] = []
        USER_NOT_SELECTED_MESSAGE_DELEGATE()

        if 'unsent' in message_dict:
            Data.chats[username].append({'sender': 'target', 'message': message_dict['message']})
            Data.save_data(f'{PORT}.bin')
            return
        if GET_SELECTED_USER_NAME() == username:
            RECEIVE_MESSAGE_DELEGATE_TARGET(message_dict['message'])
        else:
            Data.chats[username].append({'sender': 'target', 'message': message_dict['message']})
            Data.save_data(f'{PORT}.bin')
    else:
        RECEIVE_MESSAGE_DELEGATE_CLIENT(message_dict['message'])


def receive() -> None:
    while running:
        try:
            message = client.recv(1024)
            decoded_message = message.decode('utf-8')

            messages = decoded_message.split('}')
            messages = [loads(message + '}') for message in messages if message != '']

            for message in messages:
                handle_message(message)

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
          receive_message_delegate_client: Callable[[str], None],
          user_not_selected_message_delegate: Callable[[], None],
          get_selected_user_name: Callable[[], None]) -> None:
    global PORT, TARGET_PORT, HOST, client, RECEIVE_MESSAGE_DELEGATE_TARGET, RECEIVE_MESSAGE_DELEGATE_CLIENT
    global USER_NOT_SELECTED_MESSAGE_DELEGATE, GET_SELECTED_USER_NAME

    RECEIVE_MESSAGE_DELEGATE_TARGET = receive_message_delegate_target
    RECEIVE_MESSAGE_DELEGATE_CLIENT = receive_message_delegate_client
    USER_NOT_SELECTED_MESSAGE_DELEGATE = user_not_selected_message_delegate
    GET_SELECTED_USER_NAME = get_selected_user_name

    HOST = '127.0.0.1'

    client = socket(AF_INET, SOCK_STREAM)
    client.bind((HOST, PORT))
    client.connect((HOST, 5000))

    thread_receive = Thread(target=receive)
    thread_receive.start()


def stop() -> None:
    global running
    running = False
    client.close()
