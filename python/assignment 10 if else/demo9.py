""".Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime"""
import math
n=int(input("Enter number :"))
ecount=0
ocount=0
while n>0:
    d=n%10
    n=n//10
    if d%2==0:
       ecount=ecount+1
    else:
       ocount=ocount+1
dif=abs(ecount-ocount)

print("even count :",ecount)
print("odd count :",ocount)
print("diffferbece :",dif)
s=int(math.sqrt(dif))
if dif<2:
    print("not prime")
else:
    for i in range(2,s+1):
        if dif%i==0:
           print("Not prime")
           break
    else:
        print("prime")    

