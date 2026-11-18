import mysql.connector
print("program started")

conn=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="practise"
    )
cursor=conn.cursor()
#cursor.execute("create table dbemp(id int primary key auto_increment,name varchar(20),salary decimal(10,2))")
#print("table created succesfully")
cursor.execute("set autocommit=1")
name=input("enter name:")
salary=int(input("Enter salary:"))
cursor.execute(f"insert into dbemp (name,salary) values (%s,%s)",(name,salary))
print("values inerterd succesfully")
#conn.commit()
cursor.close()
conn.close()    