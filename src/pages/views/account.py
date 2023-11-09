from customtkinter import CTk, CTkLabel, CTkTabview, CTkEntry, CTkButton
from src.pages.view_models.account import AccountViewModel


class AccountView(CTk):
    def __init__(self):
        CTk.__init__(self)
        self.title('ChatArtifico - Account')
        self.geometry('500x500')
        self.resizable(False, False)
        self.configure(fg_color='#535c68')

        self.view_model: AccountViewModel = AccountViewModel(self)

        self.header: CTkLabel = CTkLabel(self, text='ChatArtifico', font=('Roboto', 24), text_color='#dff9fb')
        self.header.pack(pady=(20, 10))

        self.tab_view: CTkTabview = CTkTabview(self, fg_color='#30336b')
        self.tab_view.pack(fill='both', expand=True, padx=20, pady=(10, 20))

        self.tab_view.add('Sign In')
        self.tab_view.add('Sign Up')
        self.tab_view.set('Sign In')

        self.sing_in_user_name: CTkLabel = CTkLabel(self.tab_view.tab('Sign In'), text='User Name', font=('Roboto', 20),
                                                    text_color='#c7ecee')
        self.sing_in_user_name.pack(padx=10, pady=5, anchor='nw')

        self.sing_in_user_name_entry: CTkEntry = CTkEntry(self.tab_view.tab('Sign In'), font=('Roboto', 15),
                                                          textvariable=self.view_model.sign_in_user_name)
        self.sing_in_user_name_entry.pack(padx=10, pady=5, anchor='nw', fill='x')

        self.sing_in_password: CTkLabel = CTkLabel(self.tab_view.tab('Sign In'), text='Password', font=('Roboto', 20),
                                                   text_color='#c7ecee')
        self.sing_in_password.pack(padx=10, pady=(20, 5), anchor='nw')

        self.sing_in_password_entry: CTkEntry = CTkEntry(self.tab_view.tab('Sign In'), font=('Roboto', 15), show='*',
                                                         textvariable=self.view_model.sign_in_password)
        self.sing_in_password_entry.pack(padx=10, pady=5, anchor='nw', fill='x')

        self.sing_in_button: CTkButton = CTkButton(self.tab_view.tab('Sign In'), text='Sign In', font=('Roboto', 15),
                                                   fg_color='#7ed6df', hover_color='#22a6b3', text_color='#130f40',
                                                   height=40, command=self.view_model.open_chat_page)
        self.sing_in_button.pack(padx=10, pady=(20, 5), expand=True, fill='x')

        self.sing_up_user_name: CTkLabel = CTkLabel(self.tab_view.tab('Sign Up'), text='User Name', font=('Roboto', 20),
                                                    text_color='#c7ecee')
        self.sing_up_user_name.pack(padx=10, pady=5, anchor='nw')

        self.sing_up_user_name_entry: CTkEntry = CTkEntry(self.tab_view.tab('Sign Up'), font=('Roboto', 15),
                                                          textvariable=self.view_model.sign_up_user_name)
        self.sing_up_user_name_entry.pack(padx=10, pady=5, anchor='nw', fill='x')

        self.sing_up_password: CTkLabel = CTkLabel(self.tab_view.tab('Sign Up'), text='Password', font=('Roboto', 20),
                                                   text_color='#c7ecee')
        self.sing_up_password.pack(padx=10, pady=(20, 5), anchor='nw')

        self.sing_up_password_entry: CTkEntry = CTkEntry(self.tab_view.tab('Sign Up'), font=('Roboto', 15), show='*',
                                                         textvariable=self.view_model.sign_up_password)
        self.sing_up_password_entry.pack(padx=10, pady=5, anchor='nw', fill='x')

        self.sing_up_button: CTkButton = CTkButton(self.tab_view.tab('Sign Up'), command=self.view_model.sign_up,
                                                   text='Sign Up', font=('Roboto', 15), fg_color='#7ed6df',
                                                   hover_color='#22a6b3', text_color='#130f40', height=40)
        self.sing_up_button.pack(padx=10, pady=(20, 5), expand=True, fill='x')
