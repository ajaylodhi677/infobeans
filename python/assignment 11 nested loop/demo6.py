"""6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191 """

a=int(input(" Enter first number "))
b=int(input(" Enter second number "))
print("Palindrome are ")
for n in range(a,b+1):
    temp=n
    rev=0
    for i in range(1,len(str(n))+1):
        d=n%10
        rev=rev*10+d
        n=n//10
    if temp==rev:
          print(rev,end=" ")
