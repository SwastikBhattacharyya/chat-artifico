from pickle import dump, load


class Data:
    chats: dict[str, list] = {}

    @classmethod
    def save_data(cls, file_path: str):
        with open(file_path, 'wb') as file:
            dump(cls.chats, file)

    @classmethod
    def load_data(cls, file_path: str):
        with open(file_path, 'rb') as file:
            cls.chats = load(file)

    @classmethod
    def file_exists(cls, file_path: str) -> bool:
        try:
            with open(file_path, 'rb') as file:
                return True
        except FileNotFoundError:
            return False
