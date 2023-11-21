from socket import socket, AF_INET, SOCK_STREAM, error
from threading import Thread
from json import loads, dumps
from pprint import pprint
from pickle import dump, load

HOST = '127.0.0.1'
PORT = 5000
is_running = True

server: socket = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients: list[socket] = []
connected_ports: list[int] = []
unsent_messages: dict[int, list] = {}


def broadcast(message: bytes) -> None:
    message_dict = loads(message.decode('utf-8'))
    sender_port = message_dict['sender_port']
    target_port = message_dict['target_port']

    for client in clients:
        if client.getpeername()[1] == target_port or client.getpeername()[1] == sender_port:
            client.send(message)

    if target_port not in connected_ports:
        if target_port not in unsent_messages:
            unsent_messages[target_port] = []
        unsent_messages[target_port].append(message)


def broadcast_unsent(message: bytes) -> None:
    message_dict = loads(message.decode('utf-8'))
    message_dict['unsent'] = True
    target_port = message_dict['target_port']

    message = dumps(message_dict).encode('utf-8')

    for client in clients:
        if client.getpeername()[1] == target_port:
            client.send(message)


def handle_client(client: socket) -> None:
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except error:
            connected_ports.remove(client.getpeername()[1])
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break


def receive() -> None:
    while True:
        try:
            client, address = server.accept()
            clients.append(client)
            connected_ports.append(address[1])

            if address[1] in unsent_messages:
                for message in unsent_messages[address[1]]:
                    broadcast_unsent(message)
                unsent_messages.pop(address[1])
            thread = Thread(target=handle_client, args=(client,))
            thread.start()
        except error:
            break


def save_unsent_messages() -> None:
    global unsent_messages
    with open('unsent_messages.pickle', 'wb') as file:
        dump(unsent_messages, file)


def load_unsent_messages() -> None:
    global unsent_messages
    try:
        with open('unsent_messages.pickle', 'rb') as file:
            unsent_messages = load(file)
    except FileNotFoundError:
        unsent_messages = {}


def command_line() -> None:
    while True:
        command: str = input('>>> ')
        if command == 'quit':
            server.close()
            print('Server closed')
            save_unsent_messages()
            exit(0)
        elif command == 'length clients':
            print(len(clients))
        elif command == 'list clients':
            pprint(connected_ports)
        elif command == 'length unsent':
            print(len(unsent_messages))
        elif command == 'list unsent':
            pprint(unsent_messages)
        elif command == 'save unsent':
            save_unsent_messages()
            print('Unsent messages saved')
        elif command == 'load unsent':
            load_unsent_messages()
            print('Unsent messages loaded')
        else:
            print('Invalid command')


if __name__ == '__main__':
    print('Server started')
    load_unsent_messages()
    receive_thread = Thread(target=receive)
    receive_thread.start()
    command_line_thread = Thread(target=command_line)
    command_line_thread.start()
