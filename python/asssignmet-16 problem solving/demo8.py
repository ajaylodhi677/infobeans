"""8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number"""

n=int(input("Enter number :"))
c=n*n*n
temp=n
while n>0:
    d=n%10
    e=c%10
    if d!=e:
       print("not trimorphic number :")
       break
    n=n//10
    c=c//10
else:
   print("trimorphic number :")

