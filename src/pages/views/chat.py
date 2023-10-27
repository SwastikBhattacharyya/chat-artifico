from customtkinter import CTkToplevel, CTkFrame, CTkScrollableFrame, CTkLabel, CTkEntry, CTkButton, CTkTextbox


class ChatView(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('ChatArtifico - Chat')
        self.geometry('1280x720')
        self.resizable(False, False)
        self.configure(fg_color='#30336b')

        self.add_contact_frame: CTkFrame = CTkFrame(self, fg_color='#95afc0', width=300, height=170, corner_radius=0)
        self.add_contact_frame.place(x=10, y=10, anchor='nw')

        self.add_contact_frame_header: CTkLabel = CTkLabel(self.add_contact_frame, text='Add Contact',
                                                           font=('Roboto', 20))
        self.add_contact_frame_header.place(relx=0.5, rely=0.05, anchor='n')

        self.add_contact_user_name: CTkLabel = CTkLabel(self.add_contact_frame, text='User Name', font=('Roboto', 20))
        self.add_contact_user_name.place(relx=0.05, rely=0.45, anchor='w')

        self.add_contact_user_name_entry: CTkEntry = CTkEntry(self.add_contact_frame, font=('Roboto', 15))
        self.add_contact_user_name_entry.place(relx=0.95, rely=0.45, anchor='e')

        self.add_contact_button: CTkButton = CTkButton(self.add_contact_frame, text='Add', font=('Roboto', 15),
                                                       fg_color='#badc58', hover_color='#6ab04c', text_color='#130f40')
        self.add_contact_button.place(relx=0.5, rely=0.95, anchor='s')

        self.contacts_list_frame: CTkScrollableFrame = CTkScrollableFrame(self, fg_color='#535c68', width=300,
                                                                          height=530, corner_radius=0)
        self.contacts_list_frame.place(x=10, y=180, anchor='nw')

        #for i in range(100):
            #CTkButton(self.contacts_list_frame, height=50, text=f'Contact {i}', font=('Roboto', 15), corner_radius=0).pack(expand=True, fill='x')

        self.contact_frame: CTkFrame = CTkFrame(self, fg_color='#95afc0', width=960, height=60, corner_radius=0)
        self.contact_frame.place(x=310, y=10, anchor='nw')

        self.contact_frame_header: CTkLabel = CTkLabel(self.contact_frame, text='Contact', font=('Roboto', 20))
        self.contact_frame_header.place(relx=0.5, rely=0.5, anchor='center')

        self.messages_frame: CTkScrollableFrame = CTkScrollableFrame(self, fg_color='#130f40', width=944, height=580,
                                                                     corner_radius=0)
        self.messages_frame.place(x=310, y=70, anchor='nw')

        #for i in range(100):
           #CTkButton(self.messages_frame, width=400, text=f'Message {i}', font=('Roboto', 15), corner_radius=10).pack(padx=10, pady=10, anchor='e')

        self.typing_frame: CTkFrame = CTkFrame(self, fg_color='purple', width=960, height=60, corner_radius=0)
        self.typing_frame.place(x=310, y=650, anchor='nw')

        self.typing_entry: CTkTextbox = CTkTextbox(self.typing_frame, font=('Roboto', 15), corner_radius=0)
        self.typing_entry.place(relx=0, rely=0.5, anchor='w', relwidth=0.8, relheight=1)

        self.typing_button: CTkButton = CTkButton(self.typing_frame, text='Send', font=('Roboto', 15), corner_radius=0,
                                                  fg_color='#ffbe76', hover_color='#f0932b', text_color='#130f40')
        self.typing_button.place(relx=0.8, rely=0.5, relheight=1, relwidth=0.2, anchor='w')
