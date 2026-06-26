"""8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4"""
a=int(input("Enter start range"))
b=int(input("Enter end range"))
count=0
for a in range(a,b+1):
    if a%5==0:
       count=count+1
print("eligible tokens :",count)