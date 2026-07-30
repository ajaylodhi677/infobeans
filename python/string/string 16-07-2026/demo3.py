"""
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:


e
"""
n=input("Enter string :")
i=0
s=""
while i<len(n):
    ch=n[i]
    j=0
    c=0
    while j<len(n):
         cs=n[j]
         if ch==cs:
            c=c+1
         j=j+1
    if c==1:
      s=ch
      break
    i=i+1
    
print(s)