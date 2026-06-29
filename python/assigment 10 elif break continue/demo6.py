"""6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number"""

n=int(input("enter number :"))

num =n*n
last=0
last1=0

"""for i in range(len(str(n))):
    d=num%10
    last =last*10+d
    num=num//10
for j in range(len(str(n))):
    last1=last1*10+last%10
    last =last//10
           
if n==last1:
    print("automorphic number")
else:
    print("not automorphic number")"""

for i in range(len(str(n))):
    d=num%10
    num =num//10
    e=n%10
    n=n//10
    if e!=d:
       print("not automorphic number")
       break
else:
    print("automorphic number")


