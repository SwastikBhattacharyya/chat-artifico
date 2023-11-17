from customtkinter import CTkButton


class UserChatButton(CTkButton):
    def __init__(self, master, user_name: str, **kw):
        CTkButton.__init__(self, master, font=('Roboto', 15), fg_color='#686de0', hover_color='#4834d4',
                           text_color='#dff9fb', border_color='#dff9fb', border_width=2,
                           corner_radius=0, height=60, **kw)
        self.user_name = user_name
        self.configure(text=user_name)
