"""7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime"""
import math
n=int(input("Enter number :"))
sum=0
for i in range(1,len(str(n))+1):
    d=n%10
    n=n//10
    if i%2!=0:
       print(d,end=" ")
       sum=sum+d
print("\nAlternate sum:",sum)
m=int(math.sqrt(sum))
if sum<2:
    print("Not prime ")
else:
    for i in range(2,m+1):
       if sum%i==0:
          print("Not prime")
          break
    else:
       print("Prime:")

