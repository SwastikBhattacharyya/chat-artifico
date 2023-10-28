from customtkinter import CTkScrollableFrame, CTkButton


class ChatViewModel:
    def create_chat_box_client(self, message: str, frame: CTkScrollableFrame):
        CTkButton(frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10).pack(padx=10,
                                                                                                         pady=10,
                                                                                                         anchor='e')

    def create_chat_box_target(self, message: str, frame: CTkScrollableFrame):
        CTkButton(frame, width=400, height=50, text=message, font=('Roboto', 15), corner_radius=10).pack(padx=10,
                                                                                                         pady=10,
                                                                                                         anchor='w')
