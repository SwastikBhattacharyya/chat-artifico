# ChatArtifico

---
ChatArtifico is a sockets based chat application that allows users to communicate with each other in real time.
It is written in Python and uses the customtkinter library for the GUI. The application is written in python 3.11.

## Features
- [x] **Real time chat**: Users can send messages to each other in real time.
- [x] **GUI**: The application has a GUI that allows the user to interact with the application easily.
- [x] **User** authentication: Users can create accounts and log in to the application.
- [x] **Offline Client Handling**: The server can handle clients that are offline. Storing their messages and sending 
them when they log in.
- [x] **Server Command line**: The server has a command line that allows the admin to check connected users and any unsent
messages.
- [x] **No chat storing on server**: The server does not store any chat history. It only stores unsent messages only for the
time the user is logged out. Chat privacy of the users is maintained.
- [x] **Server and client handling using multithreading**: The server and client are both implemented using multithreading
allowing for multiple clients to connect to the server at the same time and performance gains for both the user and the
server.
- [x] **Local storage of user chats**: The client stores the chat history of the user locally in a text file. This allows
the user to view their chat history.


## Libraries used
- socket
- threading
- python-dotenv
- customtkinter
- CTkMessagebox
- pymongo

## Installation
1. Clone the repository
2. Open the project in PyCharm
3. Add an interpreter if not already present
4. Install the required libraries using `pip install -r requirements.txt`
5. Run the server.py file
6. Run the app.py file
