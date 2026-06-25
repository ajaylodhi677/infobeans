"""10. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20"""

a=int(input("Enter  I st number  "))
b=int(input("Enter IInd number  "))

print("Even number from",a, "to ",b)
for i in range(a,b+1):
    if i%2==0:
       print(i,end=" ")