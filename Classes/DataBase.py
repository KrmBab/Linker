import os
import sqlite3 as db


class DataBase:
    def __init__(self, path: str):
        self.__path = path
        db_exist = os.path.exists(self.__path)
        if not db_exist:
            folder_path = os.path.dirname(self.__path)
            os.makedirs(folder_path, exist_ok=True)

        self.__mydb = db.connect(self.__path)
        self.__cursor = self.__mydb.cursor()

        query_itms = lambda table: \
            f'''
                CREATE TABLE IF NOT EXISTS {table} (
                    "name"	TEXT NOT NULL UNIQUE,
                    "path"	TEXT NOT NULL UNIQUE,
                    "class"	TEXT,
                    FOREIGN KEY("class") REFERENCES "class_apps"("class_name"),
                    UNIQUE("name")
                )
            '''
        query_class = lambda table_class: \
            f'''
                CREATE TABLE IF NOT EXISTS {table_class} (
                    "class_name"	TEXT NOT NULL UNIQUE,
                    PRIMARY KEY("class_name")
                )
            '''

        [self.__cursor.execute(query_itms(tbl)) for tbl in ["apps", "files", "folders"]]
        [self.__cursor.execute(query_class(cls)) for cls in ["class_apps", "class_files", "class_folders"]]
        self.__mydb.commit()

    def __del__(self):
        self.__mydb.close()

    def get_class(self, className: str):
        # Construct the SQL query to select all names from the "app" table
        query = f'SELECT class_name FROM {className}'
        # Execute the query to retrieve all names
        self.__cursor.execute(query)
        # Fetch all results and store them in an array
        return [row[0] for row in self.__cursor.fetchall()]

    def set_class(self, table: str, name: str, class_name: str) -> str:
        try:
            query = f'UPDATE {table} SET class = "{class_name}" WHERE name = "{name}"'
            self.commit(query)
            return None
        except:
            return f"{name} is already exist on you {table} list"

    def add_class(self, table: str, class_name: str) -> str:
        try:
            query = f'INSERT INTO {table} (class_name) VALUES ("{class_name}")'
            self.commit(query)
            return None
        except:
            return f"{class_name} is already exist on you {table} list"

    def remove_class(self, table: str, class_name: str) -> str:
        try:
            query = f'DELETE FROM {table} WHERE class_name = "{class_name}"'
            self.commit(query)
            return None
        except:
            return f"error remove {class_name} from {table}"

    def add_item(self, table: str, name: str, path: str) -> str:
        try:
            query = f'INSERT INTO {table} (name, path) VALUES ("{name}", "{path}")'
            self.commit(query)
            return None
        except:
            return f'{name} is already exist on you {table} list'

    def delete_item(self, table: str, name: str):
        query = f'DELETE FROM {table} WHERE name = "{name}"'
        self.commit(query)

    def get_item_path(self, table: str, name: str) -> str:
        query = f'SELECT path FROM {table} WHERE name = "{name}"'
        self.__cursor.execute(query)
        return self.__cursor.fetchone()[0]  # Fetch one row

    def change_item_name(self, table: str, old_name: str, new_name: str):
        query = f'UPDATE {table} SET name = "{new_name}" WHERE name = "{old_name}"'
        try:
            self.commit(query)
        except db.Error as e:
            print(f"SQLite error: {e}")

    def get_all_names(self, table_name: str, calss_name: str) -> [str]:
        # Construct the SQL query to select all names from the "app" table
        if calss_name == "All":
            query = f'SELECT name FROM {table_name}'
        else:
            query = f'SELECT name FROM {table_name} WHERE class == "{calss_name}"'
        # Execute the query to retrieve all names
        self.__cursor.execute(query)
        # Fetch all results and store them in an array
        k = [row[0] for row in self.__cursor.fetchall()]
        return k

    def commit(self, query: str):
        self.__cursor.execute(query)
        self.__mydb.commit()
