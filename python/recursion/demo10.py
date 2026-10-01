"""
6.
 Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number
"""
def prime(n,a=2):
   if n<2:
      return "non prime"
   if n==2:
      return "prime number"
   if n%a==0:
      return "non prime"
   if a>n//2:
      return "prime number"
   return prime(n,a+1)

print(prime(int(input("Enter number:"))))