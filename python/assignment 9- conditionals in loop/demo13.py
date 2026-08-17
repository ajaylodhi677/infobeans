"""6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)"""

amount = int(input("Amount :"))
loca = input("Location :").lower()
device =input("Device type:").lower()
transaction=int(input("transaciont count :"))

if amount>=50000:
    if loca=='international':
       if device=='new':
          if transaction>=3:
             print("Risk level :High risk(block)")
          else:
             print("Risk level : medium risk")
       else:
          print("Risk level :medium risk")
    elif transaction>=5:
       print("Risk level : medium risk")
    else:
       print("Risk level :low risk")
else:
   unusual=input("unusal activity yes/no:").lower()
   if unusual=='yes':
      if device=='new':
         print("Risk level : medium risk")
      else:
         print("Risk level : low risk")
   else:
      print("Risk level : safe")
      