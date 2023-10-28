from socket import socket, AF_INET, SOCK_STREAM, error
from threading import Thread
from random import randint


HOST = '127.0.0.1'
PORT = randint(49152, 65535)

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
        client.send(message.encode('utf-8'))


if __name__ == '__main__':
    thread_receive = Thread(target=receive)
    thread_send = Thread(target=send)
    thread_receive.start()
    thread_send.start()
