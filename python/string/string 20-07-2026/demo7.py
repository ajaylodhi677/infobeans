"""
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password"""

s=input("Enter passwprd :")

if len(s)<10 or " " in s :
    print("Not strong password :")
else:
   i=0
   d=0
   u=0
   l=0
   symbol=0
   while i<len(s):
      ch=s[i]
      if ch.isdigit():
          d=1
      elif ch.isupper():
          u=1
      elif ch.islower():
          l=1
      else:
          symbol=1
      if i<len(s)-1:
         if s[i] == s[i+1]:
           print("Not strong password :")
           break
      i=i+1
   else:
      if d==1 and u==1 and l==1 and symbol==1:
        print("Strong password:")
      else:
        print("Not strong password ")
          
          
          