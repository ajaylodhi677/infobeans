"""
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password"""

n=input("Enter password ")
if len(n)<8 or len(n)>15 or n[-1] not in "1234567890" or n[0]<'A' or n[0]>'Z' or " " in n :
    print("Insecure password 1")
else :
    d=0
    s=0
    for ch in n :
       #if ch ==" " :
       #   print("Insecure password2 ")
       #   break 
       if ch in "0123456789":
          d=d+1
       if ch in "@#$%&*":
          s=s+1
    
    if d>=2 and s>=1:
        print("Secure password :")
    else:
       print("Insecure password 3")
       