'''n=int(input("Enter number line :"))

i=1
while i<=n:
    j=1
    while j<=n-i:
         print(" ",end="")
         j=j+1
    
    k=1
    while k<=2*i-1:
       print("*",end="") 
       k=k+1 
    print()
    i=i+1 
i=n-1
while i>0:
    j=n-i
    while j>0:
         print(" ",end="")
         j=j-1
    
    k=2*i-1
    while k>0:
       print("*",end="") 
       k=k-1 
    print()
    i=i-1 '''

"""n=int(input("Enter number line :"))
for i in range(1,n+1):
	print(" " * (n-i)+"*" * (2*i-1))
for i in range(n-1,0,-1):
	print(" " * (n-i)+ "*" *(2*i-1))"""

"""n=input("Enter numnbr :")
#print("Differences :",end="")
i=0
count=0
max=0
s=""
while i<len(n)-1:
    diff=abs(int(n[i])-int(n[i+1]))
    #print(diff,end=" ")
    s=s+str(diff)+""
    if diff%2==0:
       count=count+1
    if diff>max:
       max=diff
    i=i+1
print("diffeneces "," ".join(s))
print("Even diiferecens count :",count)
print("Max differnce :",max)
s=sorted(s)
if s.count(s[0])==len(s):
      print(s.count(s[0]))
      print(len(s))
      print("uniform pattern")
else:
    print("non uniform patern")"""

"""2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
"""
n=int(input("Enter number :"))
sum1=0
sum2=0
i=0
l=len(str(n))
while i<l:
     d=n%10
     if i<l//2:
        sum2=sum2+d
     else:
        sum1=sum1+d 
     n=n//10 
     i=i+1
print("first half sum ",sum1)
print("second half sum ",sum2)
if sum1==sum2:
   print("Balanced number :")
else:
   print("Unbalanced number :")    


