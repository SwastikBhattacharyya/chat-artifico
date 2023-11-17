from customtkinter import CTkScrollableFrame, CTkButton
from src.sockets.client import start, send, stop, set_target_port, get_port
from textwrap import wrap
from src.widgets.user_chat_button import UserChatButton
from src.database.database_client import DatabaseClient
from CTkMessagebox import CTkMessagebox
from tkinter import StringVar


class ChatViewModel:
    def __init__(self):
        start(self.create_chat_box_target, self.create_chat_box_client)
        self.contact_name: StringVar = StringVar()
        self.frame: CTkScrollableFrame | None = None
        self.contacts_list_frame: CTkScrollableFrame | None = None
        self.chat_boxes: list[CTkButton] = []

    def stop_client(self):
        stop()
        exit(0)

    def send_message(self, message: str):
        send(message)

    def enter_chat(self, user_name: str):
        self.destroy_chat_boxes()
        set_target_port(DatabaseClient.users_collection.find_one({'user_name': user_name})['port'])
        self.contact_name.set(user_name)

    def destroy_chat_boxes(self):
        for chat_box in self.chat_boxes:
            chat_box.destroy()
        self.chat_boxes = []

    def add_contact(self, user_name: str):
        if DatabaseClient.users_collection.find_one({'user_name': user_name}) is None:
            CTkMessagebox(title='Error', message='User not found', icon='cancel')
            return

        client_port: int = get_port()
        target_port: int = DatabaseClient.users_collection.find_one({'user_name': user_name})['port']

        if client_port == target_port:
            CTkMessagebox(title='Error', message='You cannot add yourself', icon='cancel')
            return

        button: UserChatButton = UserChatButton(self.contacts_list_frame, user_name)
        button.configure(command=lambda: self.enter_chat(button.user_name))

        button.pack(pady=(0, 1), expand=True, fill='x')

    def create_chat_box_client(self, message: str):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        self.chat_boxes.append(button)
        button.pack(padx=10, pady=10, anchor='e')
        self.frame._parent_canvas.yview_moveto('1.0')

    def create_chat_box_target(self, message: str):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        self.chat_boxes.append(button)
        button.pack(padx=10, pady=10, anchor='w')
        self.frame._parent_canvas.yview_moveto('1.0')
