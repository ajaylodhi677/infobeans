"""5.Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number"""

num=int(input("Enter number :"))
s=num%10
large=s
n=num//10
for i in range(len(str(n))):
    d=n%10
    
    if large>d:
       large=d
       n=n//10
    else:
       print("Unstable Number")
       break
else:
    print("stable number :")
