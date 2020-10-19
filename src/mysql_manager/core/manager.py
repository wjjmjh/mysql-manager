import mysql.connector


class MySQLManager:
    def __init__(self, host, db):
        self.mydb = mysql.connector.connect(
            host=host, user="remote", password="12345%$#@!"
        )
        if self.mydb.is_connected():
            print("MySQL Database has been successfully connected!")
            self.cursor = self.mydb.cursor()
            self.do("USE {};".format(db))

    def do(self, query):
        try:
            self.cursor.execute(query)
            self.mydb.commit()
        except Exception as e:
            print("method 'do' failed: {}".format(e))

    def fetch(self, query):
        try:
            self.cursor.execute(query)
            got = self.cursor.fetchall()
            got = [list(tu) for tu in got]
            return got
        except Exception as e:
            print("method 'fetch' failed: {}".format(e))
