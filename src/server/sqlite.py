import os

from pysqlcipher3 import dbapi2 as sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(os.environ["DB_NAME"])
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"PRAGMA key='{os.environ['DB_PASSWORD']}'")
        self.populate_db()

    def populate_db(self):
        # Delete table if exists
        self.__query_db("DROP TABLE IF EXISTS users;")
        # Create table
        self.__query_db(
            '''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            password TEXT NOT NULL);
            '''
        )
        # Populate new users
        users_and_pass = os.environ["USERS_AND_PASS"]
        for user_and_pass in users_and_pass.split(";"):
            self.save_user(user_and_pass.split(",")[0], user_and_pass.split(",")[1])

    def create_db(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            password TEXT NOT NULL);
            '''
        )
        self.conn.commit()

    def get_users(self):
        return self.__query_db("SELECT * FROM USERS;")

    def save_user(self, user, password):
        query = f'INSERT INTO users (user, password) VALUES ("{user}", "{password}")'
        self.cursor.execute(query)
        self.conn.commit()

    def exist_user_and_pass(self, user, password):
        query = 'SELECT * FROM users WHERE EXISTS(' \
                f'SELECT * FROM users WHERE users.user="{user}" AND users.password="{password}")'
        return self.__query_db(query)

    def __query_db(self, sql):
        self.cursor.execute(sql)

        if sql[0:6].lower() == 'select':
            return self.cursor.fetchall()
        else:
            self.conn.commit()

# if __name__ == "__main__":
#     db = Database("users.db", "grupo4")
#     db.create_db()
#     db.save_user("grupo4", "SSII_Grupo4")
#     print(db.get_users())
