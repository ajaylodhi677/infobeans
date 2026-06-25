"""*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3"""

num=int(input("Enter  number  "))
digit=int(input("Enter digit  "))

count =0
while num>0:
    a = num%10
    num=num//10
    if a==digit:
       count=count+1

print(digit,"appears ",count," times")
    
