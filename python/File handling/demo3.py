"""
3. Online Shopping Order History

An e-commerce company maintains order information in orders.txt.

Each order contains:

OrderID,CustomerName,Product,Quantity,Price
Task

Write a program to:

Accept order details.
Store them in the file.
Read the file.
Calculate total amount for each order.
Display the order having the highest total amount.

Formula:

Total Amount = Quantity × Price
Sample Input
Enter number of orders: 3

O101,Rahul,Laptop,1,55000
O102,Priya,Mouse,3,800
O103,Amit,Keyboard,2,1500
Expected Output
Order Details
--------------------------------
O101 Rahul Laptop   Quantity: 1 Total: 55000
O102 Priya Mouse    Quantity: 3 Total: 2400
O103 Amit Keyboard  Quantity: 2 Total: 3000

Highest Order:
Order ID: O101
Customer: Rahul
Total Amount: 55000
================
"""
try:
    with open("orders.txt","w+") as o:
        n=int(input("Enter number of orders:"))
        print(" in order id,customer name,product,quantity,price ")
        for i in range(n):
            print(f"Enter details for {i+1} order ")
            id,name,product,qty,price=input().split(",")
            o.write(id+","+name+","+product+","+qty+","+price+"\n")
        o.seek(0)    
        high=[]
        h=0
        print()
        for line in o:
            parts=line.split(",")
            total=int(parts[3])*int(parts[4])
            print(parts[0],parts[1],parts[2],"  Quantity :",parts[3],"Total :",total)
            if h<total:
                h=total
                high=parts

        print("\nHighest order :")
        print("Order id:",high[0])
        print("Customer name:",high[1])
        print("Total amount:",h)
except Exception as e:
    print("error ",e)            