"""9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even"""

n=int(input("Enter number  "))
temp=n
count=0

for i in range(len(str(n))):
    num=n%10
    n=n//10
    if num%2==0:
       count=count+1
if count==len(str(temp)):
   print("all even")
else:
   print("Not all even")


