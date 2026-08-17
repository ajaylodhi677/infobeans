"""9.

 Bike Service Kilometer Checker


A bike needs service every 3000 km.


Write a program to:


- Read travelled kilometers

- Print every service checkpoint till entered km


Input:

10000


Output:

3000 6000 9000"""
n=int(input("Enter kilometers :"))
if n<3000:
    print(" no service requird")
else:
    i=3000
    while i<=n:
       print(i ,end=" ")
       i=i+3000
      


