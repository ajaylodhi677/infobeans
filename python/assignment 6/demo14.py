"""14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000"""

course = input("choose course category \n press \na.for programming \nb.for design \nc .for marketing ").lower()
user = input("select user type \n1 for student\n2 for working professional\n3 for others")

fees =5000 if course=='a' else 4000 if course=='b' else 3000
total=fees*0.80 if user== '1' else fees*0.90 if user=='2' else "no discount"

print(" total fees =",total)

"""if user=='1':
    fees = fees*0.80
elif user=='2':
    fees = fees*0.90
else:
    print("no discount")

print("final course fee:",fees)"""

 