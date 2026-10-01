'''
Assignment 6: Electricity Bill Calculator
An electricity board wants to calculate a customer's electricity bill based on units consumed.
Create a class ElectricityBill with the following attributes:

Consumer number
Consumer name
Units consumed
Rate per unit
Fixed charge

Create the following methods:
calculate_energy_charge() – Calculate units × rate per unit.
calculate_total_bill() – Add energy charge and fixed charge.
display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600
'''

class ElectricityBill:
    def __init__(self):
        
        self.number = int(input("Enter Consumer number:"))
        self.name = input("Enter Consumer name:")
        self.unit_consumed = int(input("Enter Units consumed:"))
        self.r_p_unit = int(input("Enter Rate per unit:"))
        self.Fixed_charge = int(input("Enter Fixed charge:"))

    def calculate_energy_charge(self):
        self.e_charge = self.unit_consumed * self.r_p_unit

    def calculate_total_bill(self):
        self.total_bill = self.e_charge + self.Fixed_charge

    def display_bill(self):
        print("=="*15)
        print("Consumer Number:",self.number)
        print("Consumer Name:",self.name)
        print("Units Consumed:",self.unit_consumed)
        print("Rate Per Unit:",self.r_p_unit)
        print("Fixed Charge:",self.Fixed_charge)
        print("=="*15)
        print("Energy Charge: ",self.e_charge)
        print("Total Bill:",self.total_bill)


b1 = ElectricityBill()
b1.calculate_energy_charge()
b1.calculate_total_bill()
b1.display_bill()