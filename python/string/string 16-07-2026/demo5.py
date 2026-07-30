"""
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:


aabbccdde


Output:


5
"""

n=input("Enter string :")
i=0
s=""
c=0
while i<len(n):
    ch=n[i]
    if ch not in s:
       s=s+ch
    i=i+1
print(len(s))