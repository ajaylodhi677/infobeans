"""8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime"""
import math
n=int(input("Enter number :"))
larg=0
small=9
sum=0
while n>0:
    d=n%10
    n=n//10
    if d>larg:
       larg=d
    if d<small:
       small=d
sum=larg+small
print("smallest:",small)
print("largest :",larg)
print("sum :",sum)    

s=int(math.sqrt(sum))
if sum<2:
    print("not prime")
else:
    for i in range(2,s+1):
        if sum%i==0:
           print("Not prime")
           break
    else:
        print("prime")    


