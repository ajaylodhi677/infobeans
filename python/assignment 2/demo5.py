# tax calculator
amount = float(input("Enter total cart value"))

# calulate gst
tax = amount/100*12
total = amount+tax

print("cart :",amount)
print("tax :",tax)
print("total: " ,total)