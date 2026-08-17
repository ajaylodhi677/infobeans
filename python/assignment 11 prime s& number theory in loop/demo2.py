"""2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17"""
import math
n = int(input("Ente number :"))

count=0
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
            count=count+1
            print(n)
            break
            

