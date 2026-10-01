"""
5.
 Hospital Record System (Search Digit)


A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found
"""
def found(n,id):
    
    if n==0:
       return "digit not found"
    d=n%10
    if d==id:
       return "digit found"
    return found(n//10,id)
n=int(input("Enter patiend id :"))
id=int(input("Enter number to be found:"))
print(found(n,id))