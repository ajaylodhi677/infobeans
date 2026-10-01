"""
11.

=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
"""
s=input("Enter product sales :").title().split()
d={}
for x in sorted(s):
  d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,":",v)