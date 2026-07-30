"""
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number"""

n=input("Enter vehicle number :").lower()
if len(n)!=10 or n[2] not in "0123456789" or n[3] not in "0123456789" or n[0]<"a" or n[0]>"z" or n[1]<"a" or n[1]>"z" or " " in n:
    print("Invalid vehicle number")
else:
    print("valid number ")
      
