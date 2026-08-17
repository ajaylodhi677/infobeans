"""15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220"""

type =input("Enter vehicle type (bike , car, bus allowed)").lower()
hour =int(input("Enter hours parked"))

fees = 10*hour if type=='bike' else 20*hour if type=='car' else 50*hour

if hour>5:
    print("Total parking fee :",fees+100)
else:
    print("Total parking fee :",fees)


