from tkinter import StringVar
from customtkinter import CTk
from src.pages.views.chat import ChatView
from src.database.database_client import DatabaseClient
from CTkMessagebox import CTkMessagebox
from src.sockets.client import set_port


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

    def sign_in(self):
        users_collection = DatabaseClient.users_collection
        user = users_collection.find_one({
            'user_name': self.sign_in_user_name.get(),
            'password': self.sign_in_password.get()
        })

        if user is None:
            CTkMessagebox(title='Error', message='User name or password is incorrect.', icon='cancel')
            return

        self.sign_in_user_name.set('')
        self.sign_in_password.set('')

        set_port(user['port'])

        self.open_chat_page()

    def sign_up(self):
        users_collection = DatabaseClient.users_collection
        used_ports: list[int] = users_collection.distinct('port')
        port: int = self.get_first_usable_port(used_ports)

        if len(self.sign_up_user_name.get()) < 7:
            CTkMessagebox(title='Error', message='User name must be at least 7 characters.', icon='cancel')
            return

        if len(self.sign_up_password.get()) < 7:
            CTkMessagebox(title='Error', message='Password must be at least 7 characters.', icon='cancel')
            return

        if self.sign_up_user_name.get() not in users_collection.distinct('user_name'):
            users_collection.insert_one({
                'user_name': self.sign_up_user_name.get(),
                'password': self.sign_up_password.get(),
                'port': port
            })
        else:
            CTkMessagebox(title='Error', message='User name already exists.', icon='cancel')

        self.sign_up_user_name.set('')
        self.sign_up_password.set('')

    @staticmethod
    def get_first_usable_port(used_ports: list[int]):
        min_port: int = 29170
        max_port: int = 29998
        for port in range(min_port, max_port):
            if port not in used_ports:
                return port
