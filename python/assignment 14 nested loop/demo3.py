"""3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47"""
import math
a=int(input(" Enter first number "))
b=int(input(" Enter second number "))

for n in range(a,b+1):
    m=int(math.sqrt(n))
    if n>1:
        for i in range(2,m+1):
           if n%i==0:
              break
        else:
           print(n,end=" ") 
