"""
Count total alphabets, digits, and special characters. 
input S = "a1b!c2" 
output Alphabets: 3, Digits: 2, Special: 1 """

s= input("Enter string :")
a=0
d=0
sy=0
for ch in s:
   if ch.isalpha():
       a=a+1
   elif ch.isdigit():
       d=d+1
   else:
       sy=sy+1
print("Alphabets ",a,"Digits :",d,"Special :",sy)