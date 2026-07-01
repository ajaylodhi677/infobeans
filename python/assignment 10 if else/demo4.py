"""4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31"""

import math
n = int(input("Ente number :"))
m=int(math.sqrt(n))
prime=False
if n<2:
    print("not prime")
    print("no previous prime")
else:                       
    for i in range(2,m+1):  
        if n%i==0:
           print("not prime")
           break
    else:
        prime=True
        print("Prime Number")
if prime:
    count=0
    while count!=1: 
        n=n+1
        m=int(math.sqrt(n))
        if n<2:
           continue
        else:                       
           for i in range(2,m+1):
          
              if n%i==0:
                 break
           else:
              count=count+1
              print(n)
elif n>1:
    count=0
    while count!=1: 
        n=n-1
        m=int(math.sqrt(n))
        if n<2:
           continue
        else:                       
           for i in range(2,m+1):
          
              if n%i==0:
                 break
           else:
              count=count+1
              print(n)


