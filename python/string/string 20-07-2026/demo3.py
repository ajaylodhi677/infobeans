"""
 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8"""

s=input("Enter text :")
i=0
while i <len(s):
    ch=s[i]
    if ch.isdigit():
       if s.count(ch)==1:
           print(ch)
           break
    i=i+1
else:
   print("No unique digit found")
       