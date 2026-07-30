"""
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST"""

s=input("Enter employee name :")
passw=""
i=0

while i<len(s):
    ch=s[i]
    if i==0 or s[i-1]==" ":
       if ch<="z" and ch>="a" :
          ch=chr(ord(ch)-32)
          passw=passw+ch
    i=i+1
print(passw)