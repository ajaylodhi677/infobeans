"""7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32   """

a=int(input("Enter base number "))
b=int(input("Enter power number0"))
sum=1
for i in range(1,b+1):
    sum=sum*a

print(a,"to power",b,"=",sum)
    