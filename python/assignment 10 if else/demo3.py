"""
3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number"""
import math
n=int(input("Enter number :"))
m=int(math.sqrt(n))

if n<4:
    print("not a composite number :")
else:
    for i in range(2,m+1):
       if n%i==0: 
          print("Composite number")
          break
    else:
       print("not composite number")
