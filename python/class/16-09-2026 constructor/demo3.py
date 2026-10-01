"""
Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0
"""
class Product:
    def __init__(self):
      self.id=input("Enter Product id:")
      self.name=input("Enter Product name:")
      self.quantity=int(input("Enter Quantity:"))
      self.price=int(input("Enter Price of product:"))
    def calculations(self):
        self.total=self.quantity*self.price
        if self.total>5000:
            self.discount=self.total*0.10
        else:
            self.discount=self.total*0.05
        self.final=self.total-self.discount        
    def display(self):
        print("---------Shopping bill--------")  
        print("product Id".ljust(17),":",self.id)
        print("product Name".ljust(17),":",self.name)
        print("Quantity".ljust(17),":",self.quantity)
        print("Price per item".ljust(17),":",self.price)
        print("Total amount".ljust(17),":",self.total)
        print("Discount".ljust(17),":",self.discount)
        print("Final Amount".ljust(17),":",self.final)

p1=Product()
p1.calculations()
p1.display()