"""10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime"""
import math
n=input("Enter account number :")
num=int(n)
l=len(n)
l1=len(str(num))
zcount=l-l1
sum=0
mind=9
while num>0:
    d=num%10
    num=num//10
    sum=sum+d
    if mind>d:
       mind=d
    if d==0:
       zcount=zcount+1
print("Zero count :",zcount)
print("sum=",sum)
smul=(zcount+sum)*mind
print("smallest digit:",mind)
print("Final Resul :",smul)
s=int(math.sqrt(smul))
if smul<2:
    print("not prime")
else:
    for i in range(2,s+1):
        if smul%i==0:
           print("Not prime")
           break
    else:
        print("prime")    

