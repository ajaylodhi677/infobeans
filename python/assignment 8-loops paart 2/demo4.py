"""4. Numbers Divisible by 3 Between Two Numbers
A school is organizing a quiz competition. Only students whose roll numbers are divisible by 3 are selected for the first round. The teacher enters a roll number range and wants the system to display eligible roll numbers.
Write a program to display numbers divisible by 3 between two given numbers using loops.

Input:
10 25

Output:
12 15 18 21 24"""

a=int(input("Enter first digit "))
b=int(input("Enter second digit"))

while a<=b:
    if a%3==0:
       print(a,end=" ")
    a=a+1

