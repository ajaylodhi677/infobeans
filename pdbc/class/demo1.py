import mysql.connector
print("program started")


try:
    conn=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="practise"
    )
    if conn.is_connected():
        print("connected to database succesfully")
except Exception as e:
    print("mysql connection issue")
finally:
    print("connection closed")
print("done with code")                

cursor=conn.cursor()