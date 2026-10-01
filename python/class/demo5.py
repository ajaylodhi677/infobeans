'''
Assignment 5: Shopping Bill Calculator
 A retail shop wants to calculate the total bill for a customer.
Create a class ShoppingBill with the following attributes:

Product name
Product price
Quantity
Discount percentage
GST percentage

Create the following methods:

calculate_subtotal() – Calculate price × quantity
calculate_discount() – Calculate the discount amount.
calculate_gst() – Calculate GST on the discounted amount.
calculate_final_bill() – Calculate the final payable amount.
display_bill() – Display the complete bill details.

Formula:

Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST
'''

class ShoppingBill:
    def __init__(self):
        self.p_name = input("Enter Product Name:")
        self.price = int(input("Enter the Price:"))
        self.quantity = int(input("Enter the Price:"))
        self.d_per = int(input("Enter the Discount percentage:"))
        self.gst_per = int(input("Enter the GST percentage:"))

    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity

    def calculate_discount(self):
        self.dis_amount = self.subtotal - self.subtotal * self.d_per//100

    def calculate_gst(self):
        self.gst = self.dis_amount * self.gst_per / 100

    def calculate_final_bill(self):
       self.f_amount = self.dis_amount + self.gst

    def display_bill(self):
        print("=="*15)
        print("Product Name:",self.p_name)
        print("Product price",self.price)
        print("Quantity",self.quantity)
        print("Discount percentage",self.d_per)
        print("GST percentage",self.gst_per)
        print("=="*15)
        print("SubTotal: ",self.subtotal)
        print("Discount Amount:",self.dis_amount)
        print("GST Amount:",self.gst)
        print("Total Amount:",self.f_amount)


b1 = ShoppingBill()
b1.calculate_subtotal()
b1.calculate_discount()
b1.calculate_gst()
b1.calculate_final_bill()
b1.display_bill()