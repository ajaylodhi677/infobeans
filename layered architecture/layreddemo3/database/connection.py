import mysql.connector
class Database:
    def connect(self):
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="class"
        )
        #if connection.is_connected():
         #   print("data connected succesfully")
        return connection       