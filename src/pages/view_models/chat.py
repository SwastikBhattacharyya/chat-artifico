from customtkinter import CTkScrollableFrame, CTkButton
from src.sockets.client import start, send
from textwrap import wrap
from tkinter import StringVar


class ChatViewModel:
    def __init__(self):
        start(self.create_chat_box_target, self.create_chat_box_client)
        self.frame: CTkScrollableFrame | None = None

    def send_message(self, message: str):
        send(message)

    def create_chat_box_client(self, message: str):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        button.pack(padx=10, pady=10, anchor='e')
        self.frame._parent_canvas.yview_moveto('1.0')

    def create_chat_box_target(self, message: str):
        message = '\n'.join(wrap(message, 60))
        button = CTkButton(self.frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10)
        button.pack(padx=10, pady=10, anchor='w')
        self.frame._parent_canvas.yview_moveto('1.0')