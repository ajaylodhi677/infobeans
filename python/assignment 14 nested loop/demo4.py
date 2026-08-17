"""4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407"""
a=int(input(" Enter first number "))
b=int(input(" Enter second number "))

for n in range(a,b+1):
    temp=n
    sum=0
    if n<10 and n>1:
       continue
    else:
       for i in range(1,len(str(n))+1):
           d=n%10
           sum=sum+d**len(str(temp))
           n=n//10
       if temp==sum:
          print(temp,end=" ")

