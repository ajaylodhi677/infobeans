"""
ASSIGNMENT 3 – PRODUCT INVENTORY SYSTEM
=======================================

Create a Product class inside:

models/product.py

ATTRIBUTES:

* product_id
* product_name
* price
* quantity

TASKS:

1. Take details of 5 products from the user.

2. Create Product objects.

3. Store all objects in a list.

4. Display all products.

5. Calculate total value of each product.

   Total Value = Price × Quantity

6. Display products whose quantity is less than 10.

7. Find the product having the highest price.

8. Calculate total inventory value.

9. Search a product using Product Id.

SAMPLE INPUT:

101 Laptop 55000 5
102 Mouse 800 25
103 Keyboard 1500 12
104 Monitor 12000 7
105 Printer 9000 15

EXPECTED OUTPUT:

All Products:
101 Laptop 55000 5
102 Mouse 800 25
103 Keyboard 1500 12
104 Monitor 12000 7
105 Printer 9000 15

Product Total Values:
Laptop = 275000
Mouse = 20000
Keyboard = 18000
Monitor = 84000
Printer = 135000

Low Stock Products:
Laptop
Monitor

Highest Price Product:
Laptop = 55000

Total Inventory Value:
532000

Search Product Id: 103

Product Found:
103 Keyboard 1500 12
"""
from models import Product
products=[]
n=int(input("Enter number of products:"))
for i in range(n):
    print(f"Enter details for product {i+1}")
    product_id=int(input("Enter product id:"))
    product_name=input("Enter product name:")
    price=int(input("Enter price:"))
    quantity=int(input("Enter quantity:"))
    product=Product(product_id,product_name,price,quantity)
    products.append(product)

print("\nAll Products:")
Product.display(products)

print("\nProduct Total Values:")
Product.total_values(products)

print("\nLow Stock Products:")
Product.low_stock(products)

print("\nHighest Price Product:")
Product.highest_price(products)

print("\nTotal Inventory Value:")
Product.total_inventory_value(products)

product_id=int(input("\nSearch Product Id:"))

print("\nProduct Found:")
Product.search_product(products,product_id)