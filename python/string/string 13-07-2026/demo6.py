"""
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number"""

n=input("Enter Ticket number :").upper()
if n[0]=="P"  and n[1]=="N" and n[2]=="R" and len(n)==12:
    i=3
    count=0
    while i<len(n):
      ch=n[i]
      if ch in "01213456789":
         count=count+1
      i=i+1
    if count==9:
      print("Valid PNR number ")
    else:
      print("Invalid PNR number: ")
else:
   print("Invalid PNR number: ")    



