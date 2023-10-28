from src.pages.views.account import AccountView
from threading import Thread


def app():
    AccountView().mainloop()


if __name__ == "__main__":
    Thread(target=app).start()
