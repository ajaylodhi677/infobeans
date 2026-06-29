"""4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number"""


n = int(input("Enter number"))

sum =0
temp =n
l=len(str(temp))

for i in range(1,l+1):
    d = n%10
    n =n//10
    
    fact =1
    for j in range(1,d+1):
       fact = fact*j
       
    sum=sum+fact

if sum==temp:
    print("Strong Number")
else:
    print("not strong number")