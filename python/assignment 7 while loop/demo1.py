"""1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55"""

n=int(input("Enter point up to which days you want"))

sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("total points :",sum)