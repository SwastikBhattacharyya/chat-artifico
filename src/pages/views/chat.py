from customtkinter import CTkToplevel, CTkFrame, CTkScrollableFrame, CTkLabel, CTkEntry, CTkButton, CTkTextbox
from src.pages.view_models.chat import ChatViewModel
from src.data.data import Data


class ChatView(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('ChatArtifico - Chat')
        self.geometry('1280x720')
        self.resizable(False, False)
        self.configure(fg_color='#30336b')

        self.account_view_model: ChatViewModel = ChatViewModel()
        self.protocol('WM_DELETE_WINDOW', self.account_view_model.stop_client)

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
                                                       fg_color='#badc58', hover_color='#6ab04c', text_color='#130f40',
                                                       command=lambda: self.account_view_model.add_contact(
                                                           self.add_contact_user_name_entry.get()
                                                       ))
        self.add_contact_button.place(relx=0.5, rely=0.95, anchor='s')

        self.contacts_list_frame: CTkScrollableFrame = CTkScrollableFrame(self, fg_color='#535c68', width=300,
                                                                          height=530, corner_radius=0)
        self.contacts_list_frame.place(x=10, y=180, anchor='nw')

        self.contact_frame: CTkFrame = CTkFrame(self, fg_color='#95afc0', width=960, height=60, corner_radius=0)
        self.contact_frame.place(x=310, y=10, anchor='nw')

        self.contact_frame_header: CTkLabel = CTkLabel(self.contact_frame,
                                                       textvariable=self.account_view_model.contact_name,
                                                       font=('Roboto', 20))
        self.contact_frame_header.place(relx=0.5, rely=0.5, anchor='center')

        self.messages_frame: CTkScrollableFrame = CTkScrollableFrame(self, fg_color='#130f40', width=944, height=580,
                                                                     corner_radius=0)
        self.messages_frame.place(x=310, y=70, anchor='nw')

        self.typing_frame: CTkFrame = CTkFrame(self, fg_color='purple', width=960, height=60, corner_radius=0)
        self.typing_frame.place(x=310, y=650, anchor='nw')

        self.typing_entry: CTkTextbox = CTkTextbox(self.typing_frame, font=('Roboto', 15), corner_radius=0)
        self.typing_entry.place(relx=0, rely=0.5, anchor='w', relwidth=0.8, relheight=1)

        self.typing_button: CTkButton = CTkButton(self.typing_frame, text='Send', font=('Roboto', 15), corner_radius=0,
                                                  fg_color='#ffbe76', hover_color='#f0932b', text_color='#130f40',
                                                  command=lambda: self.account_view_model.send_message(
                                                      self.typing_entry.get('1.0', 'end-1c')))
        self.typing_button.place(relx=0.8, rely=0.5, relheight=1, relwidth=0.2, anchor='w')

        self.account_view_model.frame = self.messages_frame
        self.account_view_model.contacts_list_frame = self.contacts_list_frame
