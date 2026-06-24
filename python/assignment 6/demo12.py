"""12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680"""

amount1 = int(input("Enter bill amount"))
if amount1<=1000:
    amount =amount1*1.05
elif amount1<=5000:
    amount =amount1*1.12
else:
    amount =amount1*1.18

if amount>3000:
   amount=amount+200

print("Final bill amount:" ,amount)

