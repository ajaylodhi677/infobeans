"""
Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0
"""
class Guest:
    def __init__(self):
        self.id=input("Enter Guest id:")
        self.name=input("Enter Guest name:")
        self.days=int(input("Enter Number of days :"))
        self.charge=int(input("Enter Charge per day:"))
    def calculations(self):
        self.room_bill=self.days*self.charge
        self.gst=self.room_bill*0.12
        self.final_bill=self.room_bill+self.gst
    def display(self):
        print("----------Hotel bill----------")
        print("Guest Id".ljust(20),":",self.id)
        print("guest name".ljust(20),":",self.name)
        print("Number of days:".ljust(20),":",self.days)
        print("Room charge per day".ljust(20),":",self.charge)
        print("Room bill".ljust(20),":",self.room_bill)
        print("Gst(12%)".ljust(20),":",self.gst)
        print("Final bill".ljust(20),":",self.final_bill)
g1=Guest()
g1.calculations()
g1.display()        
