"""
Assignment 9: Product Inventory Management

A shopkeeper wants to manage the stock of a product.

Create a class Product with the following attributes:

Product ID

Product name

Price

Available quantity

Create the following methods:

add_stock() – Increase the available quantity.

sell_product() – Decrease the available quantity.

calculate_stock_value() – Calculate price × available quantity.

display_product() – Display product and stock details.

Sample operations:

Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3

Expected result:

Available Quantity: 12
Total Stock Value: 540000
"""
class Product:
    def __init__(self):
       self.name=input("Enter product name:") 
       self.id=int(input("Enter Product Id:"))
       self.price=int(input("Enter price of product:"))
       self.initial_quantity=int(input("Enter Available Quantity:"))
    def add_stock(self):
       self.add=int(input("Enter how much quantity you want to add:"))
       self.availabe_quantity=self.initial_quantity+self.add
    def sell_product(self):
       self.dec=int(input("Enter selled quantity:"))
       self.availabe_quantity=self.availabe_quantity-self.dec 
    def calculate_stock_value(self):
       self.stock_value=self.price*self.availabe_quantity
    def display_product(self):
       print("Product name:",self.name)
       print("Price :",self.price)
       print("initial Quantity:",self.initial_quantity)
       print("Add stock:",self.add)   
       print("Sell product:",self.dec)   
       print()
       print("Available quantity:",self.availabe_quantity)
       print("Total stock value:",self.stock_value)
p1=Product()
p1.add_stock()
p1.sell_product()
p1.calculate_stock_value()
p1.display_product()          