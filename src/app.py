from src.pages.views.account import AccountView
from threading import Thread
from dotenv import load_dotenv
from src.database.database_client import DatabaseClient
from dns.resolver import get_default_resolver


def app():
    AccountView().mainloop()


def run_prerequisites():
    get_default_resolver().nameservers = ['8.8.8.8']
    load_dotenv()
    DatabaseClient.connect()


if __name__ == "__main__":
    run_prerequisites()
    Thread(target=app).start()
