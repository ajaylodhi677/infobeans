"""
=========================================================
ASSIGNMENT 2: EMPLOYEE MANAGEMENT SYSTEM
=========================================================

--------
A company wants to maintain employee details, departments,
salaries, and cities using Python PDBC.

TABLE STRUCTURE
===============

Table Name: employee_pdbc

Column       Data Type
--------------------------------
eid          INT PRIMARY KEY
ename        VARCHAR(50)
department   VARCHAR(40)
salary       DECIMAL(10,2)
city         VARCHAR(30)


SAMPLE DATA
===========

eid   ename    department    salary      city
----------------------------------------------------
201   Amit     IT            45000.00    Indore
202   Priya    HR            40000.00    Bhopal
203   Rahul    IT            55000.00    Indore
204   Neha     Finance       50000.00    Ujjain
205   Karan    IT            60000.00    Indore


MENU
====

===== EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Employee
2. Display All Employees
3. Search Employee by Name
4. Update Employee Salary
5. Delete Employee
6. Exit

Enter your choice:


TASK 1: ADD EMPLOYEE
====================

INPUT
-----
Enter your choice: 1
Enter Employee ID: 206
Enter Employee Name: Anjali
Enter Department: HR
Enter Salary: 42000
Enter City: Dewas

OUTPUT
------
Employee inserted successfully.


TASK 2: DISPLAY ALL EMPLOYEES
=============================

INPUT
-----
Enter your choice: 2

OUTPUT
------
ID    Name      Department    Salary      City
----------------------------------------------------
201   Amit      IT            45000.00    Indore
202   Priya     HR            40000.00    Bhopal
203   Rahul     IT            55000.00    Indore
204   Neha      Finance       50000.00    Ujjain
205   Karan     IT            60000.00    Indore
206   Anjali    HR            42000.00    Dewas


TASK 3: SEARCH EMPLOYEE BY NAME USING LIKE
==========================================

INPUT
-----
Enter your choice: 3
Enter name to search: ra

OUTPUT
------
Matching employees:

ID    Name      Department    Salary      City
----------------------------------------------------
203   Rahul     IT            55000.00    Indore
205   Karan     IT            60000.00    Indore

NOTE
----
Use:
WHERE ename LIKE %s

Pass:
'%' + search_name + '%'


TASK 4: UPDATE EMPLOYEE SALARY
=============================

INPUT
-----
Enter your choice: 4
Enter Employee ID: 201
Enter New Salary: 48000

OUTPUT
------
Employee salary updated successfully.


TASK 5: DELETE EMPLOYEE
=======================

INPUT
-----
Enter your choice: 5
Enter Employee ID: 202

OUTPUT
------
Employee deleted successfully.


TASK 6: EXIT
============

INPUT
-----
Enter your choice: 6

OUTPUT
------
Thank you for using Employee Management System.
"""
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="pdbc13_11_2026",
    autocommit=True
)
if conn.is_connected():
    print("connection established succesfully")
cursor=conn.cursor()    
#cursor.execute("create table employee_pdbc(eid int primary key auto_increment,ename varchar(50),department varchar(40),salary decimal(10,2),city varchar(30))")
#print("table created succesfully")

"""query="insert into employee_pdbc values(%s,%s,%s,%s,%s)"
n=int(input("Enter how many number of students:"))
data=[]
for i in range(n):
    print(f"Enter details for {i+1} employee:")
    eid=int(input("Enter employee ID:"))
    ename=input("Enter employee :")
    department=input("Enter department name:")
    salary=float(input("Enter salary"))
    city=input("Enter city:")
    data.append((eid,ename,department,salary,city))
cursor.executemany(query,data)
if cursor.rowcount>0:
    print("data inserted succesfully")"""

while True:
    print("""MENU
====

===== EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Employee
2. Display All Employees
3. Search Employee by Name
4. Update Employee Salary
5. Delete Employee
6. Exit
    """)    
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            
