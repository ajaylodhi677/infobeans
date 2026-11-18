'''
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

'''

import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Digvijay@12",
    database="assignments"
)
cursor=conn.cursor()

class Emp:
    def add(self,data):
        q="insert into employee_pdbc VALUES (%s,%s,%s,%s,%s)"
        try:
            cursor.execute(q,data)
            conn.commit()
            print("Employee inserted successfully.")
        except Exception as e:
            print("Emp already exist",e)

    def display(self):
        q="select * from employee_pdbc "
        cursor.execute(q)
        print(cursor.fetchall())    
    def search(self,a):
        q="select * from employee_pdbc where ename like %s"
        cursor.execute(q,("%"+a+"%",))
        for i in cursor:
            print(i)

    def Update(self,d):
        q="update employee_pdbc set salary=%s where eid=%s "
        try:
            cursor.execute(q,d)
            conn.commit()
            print("Employee salary updated successfully.")
        except Exception as e:
            print("emp not available",e)
        
    def delete(self,id):
        q="delete from employee_pdbc where eid=%s"
        try:
            cursor.execute(q,(id,))
            conn.commit()
            print("Employee deleted successfully.")
        except Exception as e :
            print("not avaliable ",e)
while True:
    print('''===== EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Employee
2. Display All Employees
3. Search Employee by Name
4. Update Employee Salary
5. Delete Employee
6. Exit''')
    n=input("Enter your choice:")
    match n:
        case "1":
            print("Add Employee")
            id=int(input("Enter Employee ID: "))
            name=input("Enter Employee Name:")
            dept=input("Enter Department:")
            salary=float(input("Enter Salary:"))
            city=input("Enter City:")
            data=(id,name,dept,salary,city)
            e=Emp()
            e.add(data)
        case "2":
            e=Emp()
            e.display()
        case "3":
            a=input("Enter name to search:")
            e=Emp()
            e.search(a)
        case "4":
            id=int(input("Enter Employee ID: "))
            n_sal=float(input("Enter New Salary:"))
            e=Emp()
            d=(n_sal,id)
            e.Update(d)
        case "5":
            id=int(input("Enter Employee ID: "))
            e=Emp()
            e.delete(id)
        case "6":
            print("Thank you for using Employee Management System.")
            break
cursor.close()
conn.close()