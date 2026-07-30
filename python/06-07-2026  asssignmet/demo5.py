"""5.

Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number"""

n=int(input("Enter number :"))
s=n*n
temp=n
while n>0:
    d=n%10
    e=s%10
    if d!=e:
       print("not automorphic number :")
       break
    n=n//10
    s=s//10
else:
   print("Automorphic number :")
