"""
1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

text
abcabcbb


Output:

text
abc


s=input("Enter string :")
i=0
s1=""
while i<len(s):
    ch=s[i]
    j=i+1
    n=""
    n=n+ch
    while j<len(s):
       cj=s[j]
       if cj not in n:
         n=n+cj
       else:
         break
       j=j+1
    print(n,end=" ")
    if len(n)>len(s1):
       if s.count(n)>1:
           s1=n
    i=i+1
print()
print(s1)"""

s=input("Enter string :")
i=0
s1=""
while i<len(s):
    j=i
    n=""
    while j<len(s):
       ch=s[j]
       n=n+ch
       if s.count(n)>1:
           #print(n)
           if len(n)>len(s1):
               s1=n
       j=j+1
    i=i+1
print()
print(s1)

