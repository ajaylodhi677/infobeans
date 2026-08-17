"""3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35"""

a = int(input("Enter first number"))
b = int(input("Enter 2nd Number"))

for i in range(a,b+1):
    d=i%10
    if d!=5:
       continue
    else:
       print(i,end=" ")
   

