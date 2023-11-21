from customtkinter import CTkScrollableFrame, CTkButton
from src.sockets.client import start, send, stop, set_target_port, get_port
from textwrap import wrap
from src.widgets.user_chat_button import UserChatButton
from src.database.database_client import DatabaseClient
from CTkMessagebox import CTkMessagebox
from tkinter import StringVar
from src.data.data import Data


class ChatViewModel:
    def __init__(self):
        start(self.create_chat_box_target, self.create_chat_box_client, self.load_contacts, self.get_selected_user_name)
        self.contact_name: StringVar = StringVar()
        self.created_contact_buttons_list: list[str] = []
        self.add_contact_user_name: StringVar = StringVar()
        self.frame: CTkScrollableFrame | None = None
        self.contacts_list_frame: CTkScrollableFrame | None = None
        self.chat_boxes: list[CTkButton] = []
        self.selected_user_name: str | None = None

    def get_selected_user_name(self) -> str | None:
        return self.selected_user_name

    def stop_client(self):
        stop()
        exit(0)

    def send_message(self, message: str):
        send(message)

    def enter_chat(self, user_name: str):
        self.destroy_chat_boxes()
        set_target_port(DatabaseClient.users_collection.find_one({'user_name': user_name})['port'])
        self.selected_user_name = user_name
        self.contact_name.set(user_name)
        self.load_chats()

    def load_chats(self):
        for message in Data.chats[self.selected_user_name]:
            if message['sender'] == 'client':
                self.create_chat_box_client(message['message'], True)
            else:
                self.create_chat_box_target(message['message'], True)

    def destroy_chat_boxes(self):
        for chat_box in self.chat_boxes:
            chat_box.destroy()
        self.chat_boxes = []

    def add_contact(self):
        user_name: str = self.add_contact_user_name.get()
        if DatabaseClient.users_collection.find_one({'user_name': user_name}) is None:
            CTkMessagebox(title='Error', message='User not found', icon='cancel')
            return

        client_port: int = get_port()
        target_port: int = DatabaseClient.users_collection.find_one({'user_name': user_name})['port']

        if client_port == target_port:
            CTkMessagebox(title='Error', message='You cannot add yourself', icon='cancel')
            return

        if user_name in Data.chats:
            CTkMessagebox(title='Error', message='User already in contacts', icon='cancel')
            return

        Data.chats[user_name] = []
        Data.save_data(f'{client_port}.bin')

        button: UserChatButton = UserChatButton(self.contacts_list_frame, user_name, self.enter_chat)
        self.created_contact_buttons_list.append(user_name)

        button.pack(pady=(0, 1), expand=True, fill='x')
        self.add_contact_user_name.set('')

    def create_chat_box_client(self, message: str, for_loading: bool = False):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        self.chat_boxes.append(button)
        if not for_loading and self.selected_user_name in Data.chats:
            Data.chats[self.selected_user_name].append({'message': message, 'sender': 'client'})
            Data.save_data(f'{get_port()}.bin')
        button.pack(padx=10, pady=10, anchor='e')
        self.frame._parent_canvas.yview_moveto('1.0')

    def create_chat_box_target(self, message: str, for_loading: bool = False):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        self.chat_boxes.append(button)
        if not for_loading and self.selected_user_name in Data.chats:
            Data.chats[self.selected_user_name].append({'message': message, 'sender': 'target'})
            Data.save_data(f'{get_port()}.bin')
        button.pack(padx=10, pady=10, anchor='w')
        self.frame._parent_canvas.yview_moveto('1.0')

    def load_contacts(self):
        for user_name in Data.chats:
            if user_name in self.created_contact_buttons_list:
                continue

            button: UserChatButton = UserChatButton(self.contacts_list_frame, user_name, self.enter_chat)
            button.pack(pady=(0, 1), expand=True, fill='x')
            self.created_contact_buttons_list.append(user_name)
