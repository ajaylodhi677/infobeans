"""2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496"""

a=int(input(" Enter first number "))
b=int(input(" Enter second number "))

for n in range(a,b+1):
    sum=0
    for i in range(1,n//2+1):
           if n%i==0:
              sum=sum+i
    if temp==sum:
       print(n,end=" ")