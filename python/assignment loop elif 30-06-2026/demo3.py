"""3. Perfect Number Reward System


A gaming company rewards users if entered number is a Perfect Number.


(Perfect Number = sum of proper factors equals number)


Write a program using for-else loop to:


- Find sum of proper factors

- If sum equals number print Reward Unlocked

- Else print Try Again"""

n=int(input("Enter number :"))
sum=0
for i in range(1,n):
    if n%i==0:
       sum=sum+i
print("sum :")
if n==sum:
    print("Reward unlocked")
else:
    print("Try again ")
   


