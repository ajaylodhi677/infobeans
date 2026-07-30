"""
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda


n=input("Enter string :")+" "
i=0
s=""
while i<len(n):
    if i+1<len(n) and n[i] !=n[i+1]:
        s=s+n[i]
    i=i+1
print(s)

n=input("Enter string: ")
i=0
s=""
while i<len(n)-1:
    if n[i]!=n[i+1]:
        s=s+n[i]
    i=i+1

s=s+n[len(n)-1]
print(s)"""

n=input("Enter string :")
s=n[0]
i=1
while i<len(n):
   if n[i]!=n[i-1]:
      s=s+n[i]
   i=i+1
print(s)