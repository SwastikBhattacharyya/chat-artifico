from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

HOST = '127.0.0.1'
PORT = 5000

server: socket = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients: list[socket] = []


def broadcast(message: bytes) -> None:
    for client in clients:
        client.send(message)


def handle_client(client: socket) -> None:
    while True:
        message = client.recv(1024)
        broadcast(message)


def receive() -> None:
    while True:
        client, address = server.accept()
        clients.append(client)
        print(f'Connected with {address}')
        thread = Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == '__main__':
    receive()
