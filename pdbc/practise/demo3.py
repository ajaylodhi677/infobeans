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
    database="batch19",
    autocommit=True
)

if conn.is_connected():
    print("Connected successfully")

cursor=conn.cursor()


# ------------- CREATE TABLE AND RELATION WITH FOREIGN KEY ------------------

# query="create table pdbc1(id int primary key,name varchar(30),salary decimal(10,2))"
# cursor.execute(query)

# query1="create table pdbc2(pid int primary key,dname varchar(30),id int,foreign key(id) references pdbc1(id))"
# cursor.execute(query1)


# ------------------- INSERT DATA -------------------

# query="insert into pdbc1 (id,name,salary) values (1,'Aman',2000),(2,'Ankit',30000),(3,'Ajay',10000),(4,'Diggi',3000)"
# cursor.execute(query)

# query1="insert into pdbc2(pid,dname,id) values (101,'CSE',1),(102,'EC',2),(103,'ME',4),(104,'CE',2),(105,'IT',3)"
# cursor.execute(query1)

# query2="insert into pdbc2(pid,dname) values (106,'CSIT')"
# cursor.execute(query2)


# ------------------- AGGREGATE FUNCTIONS -------------------

# query="select sum(salary) from pdbc1"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)

# query="select avg(salary) from pdbc1"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)

# query="select max(salary) from pdbc1"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)


# ------------------- JOINS -------------------

# INNER JOIN

# query="select * from pdbc1 p1 join pdbc2 p2 on p1.id=p2.id"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)


# LEFT JOIN

# query="select * from pdbc1 p1 left join pdbc2 p2 on p1.id=p2.id"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)


# ------------------- SUBQUERY -------------------

# query="select * from pdbc1 where salary>(select avg(salary) from pdbc1)"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)


# ------------------- ORDER BY -------------------

# query="select salary from pdbc1 order by salary desc"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)


# ------------------- BETWEEN -------------------

# query="select * from pdbc1 where salary between 1000 and 10000"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)


# s1=float(input("Enter range 1:"))
# s2=float(input("Enter range 2:"))

# query="select * from pdbc1 where salary between %s and %s"
# cursor.execute(query,(s1,s2))
# result=cursor.fetchall()
# print(result)


# ------------------- GROUP BY AND HAVING -------------------

query="select id,count(*) from pdbc2 group by id having count(*)>1"
cursor.execute(query)
result=cursor.fetchall()
print(result)


cursor.close()
conn.close()