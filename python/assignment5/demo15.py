balance = int(input("ENter total balance"))
wdamt = int(input("Enter withdrawal amount:"))
pin = input("Enter pin correct/incorrect").lower()

if balance>=wdamt:
    if wdamt<=10000:
       if pin=='correct':
          print("Transaction successful")
       else:
          print("Invalid pin..")
    else:
       print("Limit excedded..")
else:
    print("Insufficient funds")