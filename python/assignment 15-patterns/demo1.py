"""
WAP to find sum of all integer which is divisible by 9 between 100 and 200"""

a=int(input("Enter number "))
b=int(input("Enter number 2nd"))
i=a
sum=0
while i<=b:
#for i in range(a,b+1):
    if i%9==0:
       sum=sum+i
    i=i+1
print("Sum =",sum)
