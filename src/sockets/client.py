from socket import socket, AF_INET, SOCK_STREAM, error
from threading import Thread
from json import dumps


PORT = int(input('Enter the port: '))
TARGET_PORT: int = int(input('Enter the target port: '))
HOST = '127.0.0.1'

client: socket = socket(AF_INET, SOCK_STREAM)
client.bind((HOST, PORT))
client.connect((HOST, 5000))


def receive() -> None:
    while True:
        try:
            message = client.recv(1024)
            print(message.decode('utf-8'))
        except error:
            print('An error occurred!')
            client.close()
            break


def send() -> None:
    while True:
        message = input()

        message_dict = {
            'sender_port': PORT,
            'target_port': TARGET_PORT,
            'message': message
        }
        message = dumps(message_dict)

        client.send(message.encode('utf-8'))


if __name__ == '__main__':
    thread_receive = Thread(target=receive)
    thread_send = Thread(target=send)
    thread_receive.start()
    thread_send.start()
