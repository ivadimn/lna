import sqlite3


class DBConnector:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnector, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._conn = sqlite3.connect("lna.db")

    def fetch(self, query):
        cursor = self._conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
