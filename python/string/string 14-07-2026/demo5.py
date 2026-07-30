"""
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code"""

n=input("Enter product code :")
rev=""
i=-1
while i>=-len(n) :
       ch=n[i]
       rev=rev+ch
       i=i-1
if rev==n:
   print("palindrome code :")
else:
   print("NOt palindrome code :")