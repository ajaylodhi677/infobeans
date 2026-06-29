"""9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number"""
num=int(input("Enter number"))
rev=0
x=num
count =0
for i in range(len(str(num))):
    count=count+1
    f=num%10
    rev=rev*10+f
    num=num//10


#print("reverse :",rev)
n=rev
temp=n
n=n//10
sum=0
max=0
print("step differences :",end=" ")
for i in range(len(str(n))):
    d=n%10
    e=temp%10
    dif=abs(e-d)
    temp=temp//10
    n=n//10
    sum=sum+dif
    if max<dif:
       max=dif
    print(dif,end=" ")
print("\nsum :",sum)
print("largest :",max)
if sum%count==0:
    print("balancede number: ")
else:
    print("unbalanced number :")


    
    
