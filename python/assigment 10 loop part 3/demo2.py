"""2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4"""

a = int(input("Enter first number"))
b = int(input("Enter 2nd Number"))

count=0
for i in range(a,b+1):
    if i%7 !=0:
       continue
    else:
       count=count+1
print("count =",count) 
         
    



