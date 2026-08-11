"""
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3"""

s=list(map(int, input("Enter marks: ").split()))
print(s)
print("Highest marks:",max(s))
print("LOwest marks :",min(s))
count=0
for i in s:
    if i>75:
       count=count+1
print("count above :",count)
