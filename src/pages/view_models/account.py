from tkinter import StringVar
from customtkinter import CTk
from src.pages.views.chat import ChatView


class AccountViewModel:
    def __init__(self, master: CTk):
        self.master = master
        self.sign_in_user_name: StringVar = StringVar()
        self.sign_in_password: StringVar = StringVar()
        self.sign_up_user_name: StringVar = StringVar()
        self.sign_up_password: StringVar = StringVar()

        self.chat_view: ChatView | None = None

    def open_chat_page(self):
        if self.chat_view is None or not self.chat_view.winfo_exists():
            self.chat_view = ChatView()
        else:
            self.chat_view.focus()
        self.master.withdraw()
