"""14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor"""

a = int(input("Enter first number"))
b = int(input("Enter second number"))

if a==b:
    print("both numbers are same") 
elif a<b:
    i=a
    while i<=b:
       if i==b:
           print(i)
       else:
           print(i, end="-->")
       i=i+1
else:
    i=a
    while i>=b:
         if i==b:
           print(i)
         else:
           print(i, end="-->")
         i=i-1