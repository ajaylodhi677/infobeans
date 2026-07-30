"""4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number"""

n=int(input("Enter number :"))
temp=n
product =1
sum=0
while n>0:
    d=n%10
    product=product*d
    sum=sum+d
    n=n//10
print("sum :",sum)
print("product :",product)
if sum==product:
    print("Spy number..")