"""
Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements
Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
"""
class Employee:
    def __init__(self):
        self.id=input("Enter Employee id:")
        self.name=input("Enter employee name:")
        self.salary=int(input("Enter basic salary:"))
    def calculations(self):
        self.hra=0.20*self.salary
        self.da=0.15*self.salary
        self.gross_sallary=self.salary+self.hra+self.da
    def display(self):
        print("-------Employee Sallary details---------")    
        print("Employee Id :",self.id)
        print("Employee Name:",self.name)
        print("Basic salary:",self.salary)
        print("Hra :",self.hra)
        print("Da :",self.da)
        print("Gross sallary :",self.gross_sallary) 
e1=Employee()
e1.calculations()
e1.display()           