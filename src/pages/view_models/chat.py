from customtkinter import CTkScrollableFrame, CTkButton
from src.sockets.client import start, send, stop
from textwrap import wrap
from src.widgets.user_chat_button import UserChatButton
from src.database.database_client import DatabaseClient
from CTkMessagebox import CTkMessagebox


class ChatViewModel:
    def __init__(self):
        start(self.create_chat_box_target, self.create_chat_box_client)
        self.frame: CTkScrollableFrame | None = None
        self.contacts_list_frame: CTkScrollableFrame | None = None
        self.chat_boxes: list[CTkButton] = []


    def stop_client(self):
        stop()
        exit(0)

    def send_message(self, message: str):
        send(message)

    def destroy_chat_boxes(self):
        for chat_box in self.chat_boxes:
            chat_box.destroy()
        self.chat_boxes = []

    def add_contact(self, user_name: str):
        if DatabaseClient.users_collection.find_one({'user_name': user_name}) is None:
            CTkMessagebox(title='Error', message='User not found', icon='cancel')
            return

        UserChatButton(self.contacts_list_frame, user_name, command=self.destroy_chat_boxes).pack(pady=(0, 1),
                                                                                                  expand=True, fill='x')

    def create_chat_box_client(self, message: str):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        self.chat_boxes.append(button)
        button.pack(padx=10, pady=10, anchor='e')
        self.frame._parent_canvas.yview_moveto('1.0')

    def create_chat_box_target(self, message: str):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        button.pack(padx=10, pady=10, anchor='w')
        self.frame._parent_canvas.yview_moveto('1.0')
