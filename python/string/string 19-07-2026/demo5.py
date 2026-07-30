"""
5.
Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a"""
n=input("Enter string :")
vis=""
c=0
i=len(n)-1
while i>=0:
   ch=n[i]
   j=i-1   
   while j>=0:
      if ch==n[j]:
         print(ch)
         c=1
         break  
      j=j-1
   if c==1:
      break 
   i=i-1
else:
   print("No repeating character found :")