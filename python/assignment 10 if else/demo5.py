"""5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3"""
import math
n=int(input("Enter number"))
temp=n

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
           print("next prime :",n)
diff=n-temp
print("gap :",diff)