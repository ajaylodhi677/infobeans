"""1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number"""
import math
n = int(input("Ente number :"))
m=int(math.sqrt(n))

if n<2:
    print("access denied")
else:                       # i=2
    for i in range(2,m+1):  #while i<n:
        if n%i==0:
           print("access denied")
           break
    else:
        print("access granted")

