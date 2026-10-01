"""
Assignment 7: Mobile Phone Data Usage

A mobile user wants to calculate their remaining internet data.

Create a class MobilePlan with the following attributes:

Customer name

Mobile number

Total data in GB

Used data in GB

Validity in days

Create the following methods:

calculate_remaining_data() – Calculate remaining data.

calculate_usage_percentage() – Calculate the percentage of data used.

display_plan() – Display the plan details and results.

Sample data:

Total Data: 50 GB
Used Data: 18 GB
Validity: 28 days

Expected result:

Remaining Data: 32 GB
Usage Percentage: 36.0%
"""
class MobilePlan:
    def __init__(self):
       self.name=input("Enter name:")
       self.number=int(input("Enter mobile number:"))
       self.total_data=int(input("Enter Total data in gb:"))
       self.used_data=int(input("Enter Used data in gb:"))
       self.Validity=int(input("Enter validity in days:"))
    def calculate_remaining_data(self):
        self.remain_data=self.total_data-self.used_data
    def calculate_usage_percentage(self):
        self.used_per=(self.used_data/self.total_data)*100
    def display_plan(self):
        print("Total data:",self.total_data)
        print("Used data :",self.used_data)
        print("Validity :",self.Validity)
        print("Remaining data:",self.remain_data,"Gb")
        print("Usage percentage:",self.used_per,"%")
p1=MobilePlan()
p1.calculate_remaining_data()
p1.calculate_usage_percentage()
p1.display_plan()