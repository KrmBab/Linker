import sqlite3 as db
import os

class DataBase:
    def __init__(self, path: str):
        self.__path = path
        db_exist = os.path.exists(self.__path)
        if not db_exist:
            folder_path = os.path.dirname(self.__path)
            os.makedirs(folder_path, exist_ok=True)

        self.__mydb = db.connect(self.__path)
        self.__cursor = self.__mydb.cursor()

        query = lambda table : \
            f'''
                CREATE TABLE IF NOT EXISTS {table} (
                    "name"	TEXT NOT NULL UNIQUE,
                    "path"	TEXT NOT NULL UNIQUE,
                    PRIMARY KEY("name")
                )
            '''
        [self.__cursor.execute(query(tbl)) for tbl in ["apps","files","folders"]]
        self.__mydb.commit()

    def __del__(self):
        self.__mydb.close()

    def add_item(self, table: str, name: str, path: str) -> str:
        try:
            query = f"INSERT INTO {table} (name, path) VALUES ('{name}', '{path}')"
            self.commit(query)
            return None
        except:
            return f"{name} is already exist on you {table} list"

    def delete_item(self, table: str, name: str):
        query = f"DELETE FROM {table} WHERE name = '{name}'"
        self.commit(query)

    def get_item_path(self, table: str, name: str) -> str:
        query = f"SELECT path FROM {table} WHERE name = '{name}'"
        self.__cursor.execute(query)
        return self.__cursor.fetchone()[0]  # Fetch one row

    def change_item_name(self, table:str ,old_name: str, new_name:str):
        query = f"UPDATE {table} SET name = '{new_name}' WHERE name = '{old_name}'"
        try:
            self.commit(query)
        except db.Error as e:
            print(f"SQLite error: {e}")

        # a = 0.
    def get_all_names(self, table: str) -> [str]:
        # Construct the SQL query to select all names from the "app" table
        query = f"SELECT name FROM {table}"
        # Execute the query to retrieve all names
        self.__cursor.execute(query)
        # Fetch all results and store them in an array
        return [row[0] for row in self.__cursor.fetchall()]

    def commit(self, query: str):
        self.__cursor.execute(query)
        self.__mydb.commit()
