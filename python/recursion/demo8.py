"""
4.
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password
"""
def even(n):
   d=n%10
   if n==0:
      return "strong number"
   if d%2!=0:
      return "weak password:"
   return even(n//10)
print(even(int(input("Enter number:"))))
