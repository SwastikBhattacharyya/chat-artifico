from customtkinter import CTkButton
from typing import Callable


class UserChatButton(CTkButton):
    def __init__(self, master, user_name: str, click_delegate: Callable[[str], None] | None, **kw):
        CTkButton.__init__(self, master, font=('Roboto', 15), fg_color='#686de0', hover_color='#4834d4',
                           text_color='#dff9fb', border_color='#dff9fb', border_width=2,
                           corner_radius=0, height=60, **kw)
        self.user_name = user_name
        self.click_delegate: Callable[[str], None] | None = click_delegate
        self.configure(text=user_name)
        self.configure(command=lambda: self.click_delegate(self.user_name))
