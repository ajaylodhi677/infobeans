"""
Aggregate functions 
Foreign key
Joins
Subquery
Between
Group by 
Having
Order by
"""
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    autocommit=True,
    database="pdbc_practise",

)
if conn.is_connected():
    print("connected succecfully")

cursor=conn.cursor()

#cursor.execute("create table department(dept_id int primary key,dept_name varchar(30) unique)")
#cursor.execute("create table employee (emp_id int primary key,emp_name varchar(20),dept_id int,salary decimal(10,2),foreign key(dept_id) references department(dept_id))")

# q="insert into department values (%s,%s)"
# n=int(input("Enter number of department:"))
# data=[]
# for i in range(n):
#     dept_id=int(input("Enter department id:"))
#     dept_name=input("Enter department name:")
#     data.append((dept_id,dept_name))

m=int(input("Enter number of employee:"))
data=[]
for i in range(m):
    emp_id=int(input("Enter emplyee Id:"))
    emp_name=input("Enter employee name:")
    dept_id=int(input("Enter department id:"))
    salary=float(input("Enter salary:"))
    data.append((emp_id,emp_name,dept_id,salary))
q="insert into employee values (%s,%s,%s,%s)"    
cursor.executemany(q,data)    