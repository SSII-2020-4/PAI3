# import sqlite3

# from sqlite3 import Error


# def sql_connection():
#     try:
#         con = sqlite3.connect('users.sqlite')
#         return con
#     except Error:
#         print(Error)


# def sql_table(con):
#     cursor = con.cursor()
#     cursor.execute(
#         "CREATE TABLE user(\
#             id INTEGER PRIMARY KEY, \
#             user TEXT, \
#             password TEXT)"
#     )
#     con.commit()


# con = sql_connection()
# sql_table(con)
from pysqlcipher3 import dbapi2 as sqlite3


class Database(object):
    def __init__(self, dbname):
        self.dbname = dbname

    def conn_db(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA key='mypassword'")

    def create_db(self):
        self.conn_db()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            login TEXT NOT NULL,
            passwd TEXT);
            '''
        )

        self.cursor.execute(
            '''
            INSERT INTO users (name, login, passwd)
            VALUES ("Admininstrator", "admin", "12345")
            '''
        )
        self.conn.commit()
        self.conn.close()

    def query_db(self, sql):
        self.conn_db()
        self.cursor.execute(sql)

        if sql[0:6].lower() == 'select':
            result = self.cursor.fetchall()
            self.conn.close()
            return result
        else:
            self.conn.commit()
            self.conn.close()


if __name__ == "__main__":
    db = Database("users.sqlite")
    db.create_db
