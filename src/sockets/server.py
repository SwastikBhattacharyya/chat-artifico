from socket import socket, AF_INET, SOCK_STREAM, error
from threading import Thread
from json import loads

HOST = '127.0.0.1'
PORT = 5000

server: socket = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients: list[socket] = []


def broadcast(message: bytes) -> None:
    message_dict = loads(message.decode('utf-8'))
    sender_port = message_dict['sender_port']
    target_port = message_dict['target_port']

    for client in clients:
        if client.getpeername()[1] == target_port or client.getpeername()[1] == sender_port:
            client.send(message)


def handle_client(client: socket) -> None:
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except error:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break


def receive() -> None:
    while True:
        client, address = server.accept()
        clients.append(client)
        print(f'Connected with {address}')
        thread = Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == '__main__':
    receive()
