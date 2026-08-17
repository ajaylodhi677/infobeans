"""
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
"""
from collections import namedtuple
employee=namedtuple("employee",["id","name","dept","sal"])
n=int(input("Enter number of employees :"))
emp=[]
for i in range(n):
    print("Enter details for employee:",i+1)
    id=int(input("Enter id:"))
    name=input("Enter name :")
    dept=input("Enter department :")
    salary=int(input("Enter salary :"))
    Edc=employee(id,name,dept,salary)
    emp.append(Edc)
print("Employee Details :")
larc=emp[0]
smlc=emp[0]
sum=0
itlst=[]
for x in emp:
    print(x.id,x.name,x.dept,x.sal)
    if (x.dept).lower()=="it":
        itlst.append(x)
    if x.sal>larc.sal:
        larc=x
    if x.sal<smlc.sal:
        smlc=x
    sum+=x.sal
print("\nHighest salllary employee :")
print(larc.id,larc.name,larc.dept,larc.sal)
print("\nLowest  salllary employee :")
print(smlc.id,smlc.name,smlc.dept,smlc.sal)
print("Average sallary of employee \n:",sum/n)
print("\nEmployees in it department :")
for x in itlst:
    print(x.id,x.name,x.dept,x.sal)

    


    