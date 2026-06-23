"""
9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books"""

member =input("Membership active(yes/no):").lower()
book = int(input(" book issued:"))

if member=="yes":
    print("Entery allowed")
if book<3:
   print(" Can issue more books")	