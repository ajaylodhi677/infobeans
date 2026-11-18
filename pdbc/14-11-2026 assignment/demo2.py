"""
============================================================
ASSIGNMENT 5: COMPANY DEPARTMENT AND EMPLOYEE ANALYSIS SYSTEM
============================================================

A company wants to manage departments and employees.
The system should support employee CRUD operations and analytical
queries using joins, foreign keys, and subqueries.

CONCEPTS TO PRACTICE
--------------------
1. Primary key
2. Foreign key
3. INSERT, SELECT, UPDATE, DELETE
4. INNER JOIN
5. LEFT JOIN
6. SELF JOIN
7. GROUP BY
8. HAVING
9. Aggregate functions
10. Single-row subquery
11. Multi-row subquery
12. Correlated subquery
13. LIKE operator
14. Menu-driven PDBC program


DATABASE TABLES
===============

TABLE 1: department_pdbc
------------------------
Column       Data Type
--------------------------------
dept_id      INT PRIMARY KEY
dept_name    VARCHAR(50)
location     VARCHAR(40)

SAMPLE DATA
-----------
dept_id  dept_name    location
------------------------------------
1        IT           Indore
2        HR           Bhopal
3        Finance      Indore
4        Sales        Ujjain
5        Training     Dewas


TABLE 2: employee_pdbc
----------------------
Column       Data Type
--------------------------------
emp_id      INT PRIMARY KEY
emp_name    VARCHAR(60)
salary      DECIMAL(10,2)
job_title   VARCHAR(50)
dept_id     INT
manager_id  INT NULL

Foreign keys:
dept_id references department_pdbc(dept_id)
manager_id references employee_pdbc(emp_id)

SAMPLE DATA
-----------
emp_id  emp_name  salary    job_title          dept_id  manager_id
-------------------------------------------------------------------
101     Amit      70000.00  Developer           1        NULL
102     Priya     55000.00  Tester              1        101
103     Rahul     90000.00  Manager             1        NULL
104     Neha      45000.00  HR Executive        2        NULL
105     Karan     80000.00  Finance Manager     3        NULL
106     Anjali    50000.00  Accountant          3        105
107     Vijay     40000.00  Sales Executive     4        NULL
108     Pooja     60000.00  Trainer             5        NULL


MENU
====

===== COMPANY EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Department
2. Add Employee
3. Display All Employees with Department
4. Search Employee by Name
5. Update Employee Salary
6. Update Employee Department
7. Delete Employee
8. Display Department-wise Employee Count
9. Display Department-wise Average Salary
10. Display Employees Earning More Than Average Salary
11. Display Employees Earning More Than Their Department Average
12. Display Employees Working in the IT Department
13. Display Departments Having More Than One Employee
14. Display Employee and Manager Names using Self Join
15. Display Departments with No Employees
16. Test Foreign Key Constraint
17. Exit

Enter your choice:


TASKS AND EXPECTED INPUT/OUTPUT
==============================

1. ADD DEPARTMENT
-----------------

INPUT
-----
Enter your choice: 1
Enter Department ID: 6
Enter Department Name: Research
Enter Location: Indore

OUTPUT
------
Department inserted successfully.


2. ADD EMPLOYEE
---------------

INPUT
-----
Enter your choice: 2
Enter Employee ID: 109
Enter Employee Name: Rohan
Enter Salary: 48000
Enter Job Title: Developer
Enter Department ID: 6
Enter Manager ID: 101

OUTPUT
------
Employee inserted successfully.


3. DISPLAY EMPLOYEES WITH DEPARTMENT USING INNER JOIN
------------------------------------------------------

REQUIRED OUTPUT COLUMNS
-----------------------
Employee ID
Employee Name
Job Title
Salary
Department Name
Location

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Job Title          Salary     Department
-------------------------------------------------------------------
101     Amit           Developer           70000.00   IT
102     Priya          Tester              55000.00   IT
103     Rahul          Manager             90000.00   IT
104     Neha           HR Executive        45000.00   HR
105     Karan          Finance Manager     80000.00   Finance
106     Anjali         Accountant          50000.00   Finance
107     Vijay          Sales Executive     40000.00   Sales
108     Pooja          Trainer             60000.00   Training


4. SEARCH EMPLOYEE BY NAME USING LIKE
-------------------------------------

INPUT
-----
Enter your choice: 4
Enter employee name to search: an

OUTPUT
------
Emp ID  Employee Name  Job Title       Salary
------------------------------------------------
101     Amit           Developer        70000.00
106     Anjali         Accountant       50000.00

Use:
WHERE emp_name LIKE '%an%'


5. UPDATE EMPLOYEE SALARY
-------------------------

INPUT
-----
Enter your choice: 5
Enter Employee ID: 102
Enter New Salary: 60000

OUTPUT
------
Employee salary updated successfully.


6. UPDATE EMPLOYEE DEPARTMENT
-----------------------------

INPUT
-----
Enter your choice: 6
Enter Employee ID: 107
Enter New Department ID: 5

OUTPUT
------
Employee department updated successfully.


7. DELETE EMPLOYEE
------------------

INPUT
-----
Enter your choice: 7
Enter Employee ID: 108

OUTPUT
------
Employee deleted successfully.


8. DEPARTMENT-WISE EMPLOYEE COUNT
---------------------------------

REQUIRED CONCEPTS
-----------------
INNER JOIN
GROUP BY
COUNT()

EXPECTED OUTPUT
---------------
Department  Employee Count
--------------------------
IT           3
HR           1
Finance      2
Sales        1
Training     1


9. DEPARTMENT-WISE AVERAGE SALARY
---------------------------------

REQUIRED CONCEPTS
-----------------
INNER JOIN
GROUP BY
AVG()

EXPECTED OUTPUT
---------------
Department  Average Salary
--------------------------
IT           71666.67
HR           45000.00
Finance      65000.00
Sales        40000.00
Training     60000.00


10. EMPLOYEES EARNING MORE THAN OVERALL AVERAGE SALARY
------------------------------------------------------

REQUIRED CONCEPT
----------------
Single-row subquery.

Question:
Display employees whose salary is greater than the average salary
of all employees.

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Salary
-----------------------------
101     Amit           70000.00
103     Rahul          90000.00
105     Karan          80000.00
108     Pooja          60000.00

Note:
The exact output changes if students update or delete records.


11. EMPLOYEES EARNING MORE THAN THEIR DEPARTMENT AVERAGE
--------------------------------------------------------

REQUIRED CONCEPT
----------------
Correlated subquery.

Question:
Display employees whose salary is greater than the average salary
of their own department.

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Department  Salary
------------------------------------------
103     Rahul          IT          90000.00
105     Karan          Finance     80000.00


12. EMPLOYEES WORKING IN IT DEPARTMENT
--------------------------------------

REQUIRED CONCEPT
----------------
Subquery returning one value.

Question:
Display all employees who work in the IT department.

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Salary
-----------------------------
101     Amit           70000.00
102     Priya          55000.00
103     Rahul          90000.00


13. DEPARTMENTS HAVING MORE THAN ONE EMPLOYEE
---------------------------------------------

REQUIRED CONCEPTS
-----------------
JOIN
GROUP BY
HAVING

EXPECTED OUTPUT
---------------
Department  Employee Count
--------------------------
IT           3
Finance      2


14. EMPLOYEE AND MANAGER NAMES USING SELF JOIN
----------------------------------------------

REQUIRED CONCEPT
----------------
Self join.

Question:
Display employee name and manager name.

EXPECTED OUTPUT
---------------
Employee Name  Manager Name
--------------------------
Priya          Amit
Anjali         Karan


15. DEPARTMENTS WITH NO EMPLOYEES
---------------------------------

REQUIRED CONCEPT
----------------
LEFT JOIN with IS NULL.

Question:
Display departments that do not have any employees.

EXPECTED OUTPUT
---------------
Department ID  Department Name
-----------------------------
6              Research

Note:
This output assumes department 6 was inserted and no employee
has yet been assigned to it.


16. FOREIGN KEY CONSTRAINT TEST
------------------------------

Try to insert an employee with a department ID that does not exist.

INPUT
-----
Enter your choice: 2
Enter Employee ID: 110
Enter Employee Name: Suresh
Enter Salary: 42000
Enter Job Title: Tester
Enter Department ID: 999
Enter Manager ID: 101

EXPECTED OUTPUT
---------------
Employee could not be inserted because the department ID
does not exist in the parent table.

Also test:
- Updating an employee to a non-existing department.
- Deleting a department that is referenced by employees.
- Inserting an employee with an invalid manager ID.
"""
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pdbc15_11_2026",
    autocommit=True
)
cursor=conn.cursor()
cursor.execute("create table if not exists department (dept_id int primary key,dept_name varchar(50),location varchar(40))")

#query="insert into department values (1,'IT','Indore'),(2,'HR','Bhopal'),(3,'Finance','Indore'),(4,'Sales','Ujjain'),(5,'Training','Dewas')"
#cursor.execute(query)
#print("data inserted succesfully")

cursor.execute("create table if not exists employee(emp_id int primary key,emp_name varchar(60),salary decimal(10,2),job_title varchar(50),dept_id int,manager_id int,foreign key (dept_id) references department(dept_id),foreign key (manager_id) references employee(emp_id))")

#query="insert into employee values (101,'Amit',70000,'Developer',1,NULL),(102,'Priya',55000,'Tester',1,101),(103,'Rahul',90000,'Manager',1,NULL),(104,'Neha',45000,'HR Executive',2,NULL),(105,'Karan',80000,'Finance Manager',3,NULL),(106,'Anjali',50000,'Accountant',3,105),(107,'Vijay',40000,'Sales Executive',4,NULL),(108,'Pooja',60000,'Trainer',5,NULL)"
#cursor.execute(query)

def adddepartment(dept_id,dept_name,location):
    try:
        query="insert into department values(%s,%s,%s)"
        cursor.execute(query,(dept_id,dept_name,location))
        print("Department inserted succesfully")
    except Exception as e:
        print("error :",e) 

def addEmployee(emp_id,emp_name,salary,job_title,dept_id,manager_id):
    try:
       query="insert into employee values(%s,%s,%s,%s,%s,%s)"
       cursor.execute(query,(emp_id,emp_name,salary,job_title,dept_id,manager_id))
       print("employee inserted succesfully")
    except Exception as e:
        print("Error :",e)    
def DisplayEmpDept():
     cursor.execute("select emp_id,emp_name,job_title,salary,dept_name,location from employee as e inner join department as d on e.dept_id=d.dept_id")
     res=cursor.fetchall()
     
     print("ID".ljust(8),"Name".ljust(15),"Job Title".ljust(20),"Salary".ljust(12),"Department".ljust(15),"Location".ljust(12))
     print("-"*85)
     
     for row in res:
         print(str(row[0]).ljust(8),str(row[1]).ljust(15),str(row[2]).ljust(20),str(row[3]).ljust(12),str(row[4]).ljust(15),str(row[5]).ljust(12))  
def search(emp_name):
    query="select * from employee where emp_name like %s"
    cursor.execute(query,('%'+emp_name+'%',))
    res=cursor.fetchall()

    print("ID".ljust(8),"Name".ljust(15),"Salary".ljust(12),"Job Title".ljust(20))
    print("-"*60)

    for row in res:
        print(str(row[0]).ljust(8),str(row[1]).ljust(15),str(row[2]).ljust(12),str(row[3]).ljust(20))
def UpdateSalary(emp_id,salary):
    query="update employee set salary =%s where emp_id=%s"
    try:
      cursor.execute(query,(salary,emp_id))
      if cursor.rowcount>0:
         print("employee salary updated succesfully")
      else:
        print("no record found")   
    except Exception as e:
        print("Error :",e)
def UpdateDept(emp_id,dept_id):
    query="update employee set dept_id=%s where emp_id =%s"
    try:
        cursor.execute(query,(dept_id,emp_id))
        if cursor.rowcount>0:
            print("Department updated succesfully")
        else:
            print("no recourd found")
    except Exceptionas as e:
        print("Error :",e)  
def DeleteEmp(emp_id):
    query="delete from employee where emp_id=%s"
    try:
        cursor.execute(query,(emp_id,))
        if cursor.rowcount>0:
            print("employee deleted succesfully")
        else:
            print("no record found")
    except Exception as e:
        print("Error :",e)      
def DepartmentCout():
    cursor.execute("select d.dept_id,d.dept_name,count(*) from department as d inner join employee as e on e.dept_id=d.dept_id group by d.dept_id,d.dept_name")
    res=cursor.fetchall()

    print("Dept ID".ljust(12),"Department".ljust(20),"Employee Count".ljust(15))
    print("-"*47)

    for row in res:
        print(str(row[0]).ljust(12),str(row[1]).ljust(20),str(row[2]).ljust(15)) 

def EarnAvg():
    query="select * from employee where salary>(select avg(salary) from employee)"
    cursor.execute(query)
    res=cursor.fetchall()

    print("ID".ljust(8),"Name".ljust(15),"Salary".ljust(12))
    print("-"*35)

    for row in res:
        print(str(row[0]).ljust(8),str(row[1]).ljust(15),str(row[2]).ljust(12)) 
def EarnDeptAvg():
    query="select * from employee as e where salary>(select avg(salary) from employee as e1 where e.dept_id=e1.dept_id)"
    cursor.execute(query)
    res=cursor.fetchall()

    print("ID".ljust(8),"Name".ljust(15),"Salary".ljust(12))
    print("-"*35)

    for row in res:
        print(str(row[0]).ljust(8),str(row[1]).ljust(15),str(row[2]).ljust(12)) 
def WorkIt():
    query="select * from employee where dept_id in(select dept_id from department where dept_name='it')"
    cursor.execute(query)
    res=cursor.fetchall()

    print("ID".ljust(8),"Name".ljust(15),"Salary".ljust(12),"Job Title".ljust(20))
    print("-"*55)

    for row in res:
        print(str(row[0]).ljust(8),str(row[1]).ljust(15),str(row[2]).ljust(12),str(row[3]).ljust(20))
def DeptEmp1():
    query="select dept_name,count(*) as employee_count from department as d inner join employee as e on e.dept_id=d.dept_id group by d.dept_id,dept_name having employee_count>1"
    cursor.execute(query)
    res=cursor.fetchall()

    print("Department".ljust(20),"Employee Count".ljust(15))
    print("-"*35)

    for row in res:
        print(str(row[0]).ljust(20),str(row[1]).ljust(15))
def EmpManger():
    query="select e.emp_name,m.emp_name from employee as e inner join employee as m on e.manager_id=m.emp_id"
    cursor.execute(query) 
    res=cursor.fetchall()   

    print("Employee Name".ljust(20),"Manager Name".ljust(20))
    print("-"*40)
    
    for row in res:
        print(str(row[0]).ljust(20),str(row[1]).ljust(20))  
def DeptNoEmp():          
    query="select d.dept_Id,dept_name from department as d left join employee as e on e.dept_id=d.dept_id where emp_id is null"
    cursor.execute(query)
    res=cursor.fetchall()
    
    print("Department Id".ljust(20),"Department Name".ljust(20))
    print("-"*40)
    
    for row in res:
        print(str(row[0]).ljust(20),str(row[1]).ljust(20))         
while True:
    print("""
    MENU
====

===== COMPANY EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Department
2. Add Employee
3. Display All Employees with Department
4. Search Employee by Name
5. Update Employee Salary
6. Update Employee Department
7. Delete Employee
8. Display Department-wise Employee Count
9. Display Department-wise Average Salary
10. Display Employees Earning More Than Average Salary
11. Display Employees Earning More Than Their Department Average
12. Display Employees Working in the IT Department
13. Display Departments Having More Than One Employee
14. Display Employee and Manager Names using Self Join
15. Display Departments with No Employees
16. Test Foreign Key Constraint
17. Exit
""")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1 :
            dept_id=int(input("Enter department Id:"))
            dept_name=input("Enter department name:")
            location=input("Enter location:")
            adddepartment(dept_id,dept_name,location)
        case 2 :
            emp_id=int(input("Enter employee id:"))
            emp_name=input("Enter employee name:")
            salary=float(input("Enter salary:"))
            job_title=input("enter job tittle:")
            dept_id=int(input("Enter department id:"))
            manager_id=int(input("Enter manager id:"))
            addEmployee(emp_id,emp_name,salary,job_title,dept_id,manager_id) 
        case 3:
            DisplayEmpDept() 
        case 4 :
            emp_name=input("enter employee name to search:")
            search(emp_name)
        case 5 :
            emp_id=int(input("enter employee id:"))
            salary=float(input("Enter  new salary:"))
            UpdateSalary(emp_id,salary)  
        case 6:
            emp_id=int(input("enter employee id:"))
            dep_id=int(input("Enter department id:"))
            UpdateDept(emp_id,dep_id)
        case 7 :
            emp_id=int(input("enter employee id:"))
            DeleteEmp(emp_id)
        case 8 :
            DepartmentCout()
        case 9 :
            DepartmentAvg() 
        case 10 :
            EarnAvg() 
        case 11 :
            EarnDeptAvg() 
        case 12 :
            WorkIt() 
        case 13 :
            DeptEmp1() 
        case 14 :
            EmpManger() 
        case 15 :
            DeptNoEmp() 
        case 16 :
            emp_id=int(input("Enter employee id:"))
            mp_name=input("Enter employee name:")
            salary=float(input("Enter salary:"))
            job_title=input("enter job tittle:")
            dept_id=int(input("Enter department id:"))
            manager_id=int(input("Enter manager id:"))
            addEmployee(emp_id,emp_name,salary,job_title,dept_id,manager_id)                          
        case 17 :
            print("Thanks for using employee management")
            break
        case _ :
            print("Invalid choice")
