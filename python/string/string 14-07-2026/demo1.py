"""
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
"""
u=input("Enter Username :").lower()
if u[0]<'a' or u[0]>"z" or len(u)>12 or len(u)<5 or " " in u:
   print("Not valid userName")
else:
   i=1
   under=0
   
   while i<len(u):
      ch=u[i]
      if ch=="_" or ch in "0123456789" or "a"<=ch<="z":
        under=1
      else:
        under=0
      i=i+1
   if under==1:
      print("Valid  username :")
   else:
      print("Invalid username :")