"""
============================================================
ASSIGNMENT 2 – EMPLOYEE MANAGEMENT SYSTEM
=========================================

Create an Employee class inside:

models/employee.py

ATTRIBUTES:

* employee_id
* name
* salary
* department

TASKS:

1. Take details of 5 employees from the user.
2. Create Employee objects.
3. Store the objects inside a list.
4. Display all employees.
5. Display employees whose salary is greater than 40,000.
6. Display employees who belong to the IT department.
7. Find the employee having the highest salary.
8. Calculate total salary of all employees.
9. Calculate average salary.

SAMPLE INPUT:

101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

EXPECTED OUTPUT:

All Employees:
101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

Employees with salary greater than 40000:
101 Amit 45000 IT
103 Priya 60000 IT
104 Neha 50000 Finance

Employees from IT Department:
101 Amit 45000 IT
103 Priya 60000 IT

Highest Salary Employee:
103 Priya 60000 IT

Total Salary:
220000

Average Salary:
44000
"""
from models import Employee
employees=[]

n=int(input("Enter number of employees:"))

for i in range(n):
    print(f"Enter details for employee {i+1}")
    employee_id=int(input("Enter employee id:"))
    name=input("Enter name:")
    salary=int(input("Enter salary:"))
    department=input("Enter department:")

    employee=Employee(employee_id,name,salary,department)
    employees.append(employee)

print("\nAll Employees:")
Employee.display(employees)

print("\nEmployees with salary greater than 40000:")
Employee.salary_greater_than_40000(employees)

print("\nEmployees from IT Department:")
Employee.it_department(employees)

print("\nHighest Salary Employee:")
Employee.highest_salary(employees)

print("\nTotal Salary:")
Employee.total_salary(employees)

print("\nAverage Salary:")
Employee.average_salary(employees)