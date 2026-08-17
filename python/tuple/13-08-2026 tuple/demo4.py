"""
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3"""
from collections import namedtuple 
order=namedtuple("order",["order_id","customer_name","product_name","amount"]) 
n=int(input("Enter number of orders :")) 
ord=[] 
for i in range(n): 
    print("Enter details for order :",i+1) 
    order_id=input("Enter order id :") 
    customer_name=input("Enter customer name :") 
    product_name=input("Enter product name :") 
    amount=int(input("Enter amount :")) 
    ord.append(order(order_id,customer_name,product_name,amount)) 

print("==="*20) 
print("showing details") 

hord=ord[0] 
totol=0 
ab1000=0 

for x in ord: 
    print(x.order_id,x.customer_name,x.product_name,x.amount) 
    if x.amount>hord.amount: 
        hord=x 
    totol+=x.amount 
    if x.amount>10000: 
       ab1000+=1 

print("==="*20) 
print("Highest Value Order :") 
print(hord.order_id,hord.customer_name,hord.product_name,hord.amount) 

print("==="*20) 
print("Total Sales :") 
print(totol) 

print("==="*20) 
print("Orders Above ₹10,000 :") 
print(ab1000)