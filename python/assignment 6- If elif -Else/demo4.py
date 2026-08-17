amount = int(input("Enter your bill amount"))

if amount>5000:
   amount=amount-(amount*0.20)
   print("final bill amount :",amount)
elif amount>=2000 and amount<=5000:
   amount=amount-(amount*0.10)
   print("final bill amount :",amount)
else:
   amount=amount-(amount*0.05)
   print("final bill amount :",amount)
   