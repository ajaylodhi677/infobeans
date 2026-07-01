"""2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime"""
import math
n=int(input("Enter number :"))
temp=n
sum=0
product=1
while n>0:
    d=n%10
    n= n//10
    sum=sum+d
    product=product*d
dif=abs(product-sum)
l=len(str(dif))
final=dif+l
print("Sum :",sum)
print("product :",product)
print("Difference :",dif)
print("digit :",l)
print("final result :",final)

m=int(math.sqrt(final))
if final<2:
    print("Not prime ")
else:
    for i in range(2,m+1):
       if final%i==0:
          print("Not prime")
          break
    else:
       print("Prime:")
