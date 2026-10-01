"""
Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

Employee ID

Employee name

Basic salary

HRA percentage

DA percentage

Create the following methods:

calculate_hra() – Calculate HRA.

calculate_da() – Calculate DA.

calculate_gross_salary() – Calculate gross salary.

display_salary() – Display employee salary details.

Formula:

HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA

"""
class Employee:
   def __init__(self):
       self.id=int(input("Enter Employee id:"))
       self.name=input("Enter name:")
       self.basic=int(input("Enter basic sallery:"))
       self.hrap=int(input("Enter hra percentag:"))
       self.dap=int(input("Enter da pecentrage:"))
   def calculate_hra(self):
       self.hra=self.basic*self.hrap/100
   def calculate_da(self):
       self.da=self.basic*self.dap/100
   def calculate_gross_salary(self):
       self.gross=self.basic+self.hra+self.da
   def display_salary(self):
       print("=="*15)
       print("Salllary details")
       print("Employee name:",self.name)
       print("Employee id :",self.id)
       print("=="*15)
       print()
       print("Basic sallery:",self.basic)
       print("Hra:",self.hra)
       print("Da:",self.da)
       print()
       print("Gross sallery :",self.gross)
e1=Employee()
e1.calculate_hra()
e1.calculate_da()
e1.calculate_gross_salary()
e1.display_salary()       
                
    