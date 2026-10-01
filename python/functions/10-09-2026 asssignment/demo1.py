"""
Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
"""
from datetime import datetime,timedelta
age=input("Enter Dob:")
bage=datetime.strptime(age,"%d-%m-%Y")
today=datetime.now()
a=today.year-bage.year
next=bage.replace(year=today.year+1)
rday=(next-today).days
print("Age :",a)
print("Total days:",(today-bage).days)
print("Next birthday:",datetime.strftime(next,"%d-%m-%Y"))
print("Days remaing:",rday)