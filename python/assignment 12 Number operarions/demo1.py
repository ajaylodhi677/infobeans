"""1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime"""
import math
n=int(input("Enter number :"))
org=n
rev=0
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
    rev=rev*10+d
dif=abs(org-rev)
final=dif+sum
print("Sum of digit :",sum)
print("Reverse : ",rev)
print("Differnece :",dif)
print("Final result :",final)

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
