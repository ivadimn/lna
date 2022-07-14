import sqlite3


class Connection:
    _instance : ["Connection"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.connection = sqlite3.connect("lna.db")
        print("__init__")

    def __del__(self):
        if self.connection:
            self.connection.close()

