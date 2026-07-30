"""
7.
Smart City Citizen Information Formatter

The Smart City Management Department is developing a digital portal to store citizen information in a professional format. Many citizens enter their details using small letters, uppercase letters, mixed casing, or numbers, which creates problems while generating official documents like ID cards, electricity bills, tax records, certificates, and address proofs.

To solve this issue, the department wants a program that automatically converts only the first character of every word into uppercase while keeping the remaining characters unchanged.

The input may contain:
- Words already written in uppercase
- Mixed-case words
- Numbers
- Address details
- Department names
- City names

Task:
Read a complete string from the user and convert the first character of every word into uppercase.

Conditions:
- Words may contain spaces between them
- Do not use built-in title() function
- Digits should remain unchanged

Input:
Enter citizen information:
deepika padukone from smart city raisen madhya pradesh

Output:
Formatted Information:
Deepika Padukone From Smart City Raisen Madhya Pradesh"""

n=input("Enter citizen information :")
i=0
s=""
while i<len(n) :
    ch=n[i]
    if i==0 or n[i-1]==" ":
        if ch<="z" and ch >="a" :
           ch=chr(ord(ch)-32)
          # print(ch,end="")
    s=s+ch
    i=i+1
print(s)           


