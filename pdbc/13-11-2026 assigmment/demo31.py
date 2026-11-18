"""=========================================================
ASSIGNMENT 3: PRODUCT INVENTORY MANAGEMENT SYSTEM
=========================================================

SCENARIO
--------
A retail shop wants to manage product details, prices,
categories, and available stock using Python PDBC.

CONCEPTS TO PRACTICE
--------------------
1. INSERT
2. SELECT
3. UPDATE
4. DELETE
5. LIKE operator
6. Parameterized queries
7. commit()
8. fetchall()
9. Menu-driven programming


TABLE STRUCTURE
===============

Table Name: product_pdbc

Column       Data Type
--------------------------------
pid          INT PRIMARY KEY
pname        VARCHAR(60)
category     VARCHAR(40)
price        DECIMAL(10,2)
quantity     INT


SAMPLE DATA
===========

pid   pname       category       price       quantity
------------------------------------------------------------
301   Laptop      Electronics    55000.00    10
302   Mouse       Electronics      800.00    50
303   Keyboard    Electronics     1500.00    30
304   Notebook    Stationery       100.00   100
305   Pen         Stationery        20.00   200


MENU
====

===== PRODUCT INVENTORY SYSTEM =====
1. Add Product
2. Display All Products
3. Search Product by Name
4. Update Product Price
5. Delete Product
6. Exit

Enter your choice:


TASK 1: ADD PRODUCT
===================

INPUT
-----
Enter your choice: 1
Enter Product ID: 306
Enter Product Name: Monitor
Enter Category: Electronics
Enter Price: 12000
Enter Quantity: 15

OUTPUT
------
Product inserted successfully.


TASK 2: DISPLAY ALL PRODUCTS
============================

INPUT
-----
Enter your choice: 2

OUTPUT
------
ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics     55000.00    10
302   Mouse         Electronics       800.00    50
303   Keyboard      Electronics      1500.00    30
304   Notebook      Stationery        100.00   100
305   Pen           Stationery         20.00   200
306   Monitor       Electronics     12000.00    15


TASK 3: SEARCH PRODUCT BY NAME USING LIKE
=========================================

INPUT
-----
Enter your choice: 3
Enter product name to search: o

OUTPUT
------
Matching products:

ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics     55000.00    10
302   Mouse         Electronics       800.00    50
304   Notebook      Stationery        100.00   100
306   Monitor       Electronics     12000.00    15

NOTE
----
Use:
WHERE pname LIKE %s

Pass:
'%' + search_name + '%'


TASK 4: UPDATE PRODUCT PRICE
============================

INPUT
-----
Enter your choice: 4
Enter Product ID: 302
Enter New Price: 900

OUTPUT
------
Product price updated successfully.


TASK 5: DELETE PRODUCT
======================

INPUT
-----
Enter your choice: 5
Enter Product ID: 305

OUTPUT
------
Product deleted successfully.


TASK 6: EXIT
============

INPUT
-----
Enter your choice: 6

OUTPUT
------
Thank you for using Product Inventory System.


add these scenarios also:--

1. Display all products from Electronics category.
2. Display all products from Stationery category.
3. Search products whose names contain 'oo'.
4. Search products whose names start with 'M'.
5. Search products whose names end with 'e'.
6. Display products whose price is greater than 1000.
7. Display products whose quantity is less than 20.
8. Update product quantity.
9. Update product category.
10. Delete a product by ID.
11. Display products whose category contains 'tron'.
12. Search products by a user-provided price range.



SUGGESTED SUCCESS MESSAGES
==========================

INSERT:
Record inserted successfully.

SELECT:
Records displayed successfully.

UPDATE:
Record updated successfully.

DELETE:
Record deleted successfully.

NOT FOUND:
No record found for the given ID.

INVALID CHOICE:
Invalid choice. Please try again.

EXIT:
Thank you for using the system."""


import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Digvijay@12",
    database="assignments"
)
cursor=conn.cursor()

class Product:
    def add(self,data):
        q="insert into product_pdbc values(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(q,data)
            conn.commit()
            print("Product inserted successfully.")
        except Exception as e:
            print("error",e)

    def display(self):
        q="select * from product_pdbc"
        cursor.execute(q)
        data=cursor.fetchall()
        for i in data:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
        
    def search(self,name):
        q="SELECT * FROM product_pdbc WHERE pname LIKE %s"
        cursor.execute(q,("%"+name+"%",))
        d=cursor.fetchall()
        if d:
            for i in d:
                print(i)
        else:
            print("product not found")
    def update (self,data):
        q="update product_pdbc SET price=%s WHERE pid=%s "
        cursor.execute(q,data)
        conn.commit()
        if cursor.rowcount>0:
              print("product price updated successfully.")
        else:
            print("product not found")
    def delete (self,id):
        q="DELETE FROM product_pdbc WHERE pid=%s"
        cursor.execute(q,(id,))
        conn.commit()
        if cursor.rowcount>0:
            print("delete successfully")
        else:
            print("not found")
while True:
    print('''===== PRODUCT INVENTORY SYSTEM =====
1. Add Product
2. Display All Products
3. Search Product by Name
4. Update Product Price
5. Delete Product
6. Exit''')
    n=input("Enter your choice:")
    match n:
        case "1":
            id=int(input("Enter Product ID:"))
            name=(input("Enter Product Name:"))
            cat=(input("Enter Category:"))
            price=float(input("Enter Price:"))
            quantity=int(input("Enter Quantity:"))
            data=(id,name,cat,price,quantity)
            p=Product()
            p.add(data)
        case "2":
            p=Product()
            p.display()
        case "3":
            name=input("Enter product name to search:")
            p=Product()
            p.search(name)
        case "4":
            id=int(input("Enter Product ID:"))
            price=float(input("Enter New Price: "))
            data=(price,id)
            p=Product()
            p.update(data)
        case "5":
            id=int(input("Enter Product ID:"))
            p=Product()
            p.delete(id)
        case "6":
            print("Thank you for using Product Inventory System.")
            break
        case _:
            print("invalid choice")
cursor.close()
conn.close()