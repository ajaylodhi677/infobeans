"""3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5"""

n=int(input("Enter numbers"))
rev =0
for i in range(len(str(n))):
    d=n%10
    rev=rev*10+d
    n=n//10

first=rev%10
print("First digit :",first)
"""temp=n
for i in range(len(str(temp))-1):
        n=n//10
        i=i+1
print("first digit:",n)"""


    
