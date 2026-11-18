import mysql.connector
print("program started")
conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="practise",
    autocommit=True,
    connection_timeout=10
)
if conn.is_connected:
    print("coneetion succesfully established")
else:
    print('connection failed')    

cursor=conn.cursor()
cursor.execute("show tables")    
result=cursor.fetchall()
print(result)
for row in result:
    print(row)

cursor.execute("select * from customer;")
res=cursor.fetchall()
print(res)    