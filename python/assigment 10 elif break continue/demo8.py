"""8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected

Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified"""

n =int(input("Enter numbers :"))
rev=0
temp =n

for i in range(len(str(n))):
    d =n%10
    rev =rev*10+d
    n=n//10
diff=abs(rev-temp)
temp1=diff

count=0
for i in range(len(str(diff))):
   count =count+1
   diff=diff//10

if temp1==0:
    print("reverse =",rev," Difference =",temp1, " Digit =",count,"Perfect match")
elif temp1%9==0:
    print("reverse =",rev," Difference",temp1, " Digit ",count,"Verified")
else:
    print("reject")
