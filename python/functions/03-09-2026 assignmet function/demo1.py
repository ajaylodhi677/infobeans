"""
1.
Employee Record Sorting (Lambda)


A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

Task

Write a Python program to sort the employee records using a lambda expression.

Input
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]
"""
employee=[]
n=int(input("Enter number of employees:"))
for i in range(n):
    name=input(f"Enter name of employee{i+1}:")
    salary=int(input("Enter salary :"))
    ed=(name,salary)
    employee.append(ed)
print(employee)
print("employee details in sorted form ")
result=sorted(employee,key=lambda x:x[1])
print(result)