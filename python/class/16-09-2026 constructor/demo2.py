"""
Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0
"""
class Customer:
    def __init__(self):
      self.id=input("Enter Customer id:")
      self.name=input("Enter Customer name:")
      self.unit=int(input("Enter Units consumed:"))  
    def calculations(self):
        self.total=self.unit*8+150  
    def display(self):
        print("---------Electricity--------")  
        print("Customer Id".ljust(17),":",self.id)
        print("Customer Name".ljust(17),":",self.name)
        print("Units Consumed".ljust(17),":",self.unit)
        print("Total Bill Amount".ljust(17),":",self.total)
c1=Customer()
c1.calculations()
c1.display()
           