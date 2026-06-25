"""6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong"""

n=int(input("Enter number  "))
temp =n
sum =0

while n>0:""
    num =n%10
    n=n//10
    sum=sum+num**len(str(temp))
    

if sum==temp:
    print("origional num :",temp,"\ncalculate number :",sum)
    print("number is armstron")
else:
    print("origional num :",temp,"\ncalculate number :",sum)
    print("number is  not Armstrong")
    
