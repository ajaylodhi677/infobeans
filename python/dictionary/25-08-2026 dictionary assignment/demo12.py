"""

12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
"""
s=input("Enter food order:").title().split()
d={}
for x in sorted(s):
  d[x]=d.get(x,0)+1
most=max(d.values())
for k,v in d.items():
    print(k,":",v)
    if v==most:
      print("most ordered :",k)