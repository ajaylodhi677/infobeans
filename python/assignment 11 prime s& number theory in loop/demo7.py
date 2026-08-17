"""7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number"""
import math
n=int(input("Enter numbr :"))
temp=n
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d

print("sum :",sum)
s=int(math.sqrt(sum))
if sum<2:
    print("Normal number")
else:
    for i in range(2,s+1):
        if sum%i==0:
           print("Normal number")
           break
    else:
        print("Lucky number")    
