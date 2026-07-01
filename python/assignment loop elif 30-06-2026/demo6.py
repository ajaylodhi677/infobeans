"""6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29"""
import math
n=int(input("Enter number :"))

while True:
    n=n+1
    m=int(math.sqrt(n))
    if n<2:
       continue
    else:
       for i in range(2,m+1):
          if n%i==0:
             break
       else:
          print("next prime cabin =",n)
          break