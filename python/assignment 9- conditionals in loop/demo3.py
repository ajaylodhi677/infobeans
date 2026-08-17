"""6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged"""

amount=int(input("Enter transaction amount :"))

if amount>=10000:
    loca=input("location :").lower()
    if loca=='international':
       otp=int(input("Enter otp :"))
       if otp==2346:
          print("otp verified")
          print("transaction allowed")
       else:
          print("otp invalid")
          print("traction blocked")
    elif amount>=5000:
       age=int(input("account age :"))
       if age>=2:
          print("transaction allowed")
       else:
          print("flagged")
    else:
       print("allowed")
else:
    act=input("unusal activity")
    if act=='yes':
       print("flageed")
    else:
       print("allowed")
    
       
       