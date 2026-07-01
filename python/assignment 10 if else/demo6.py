"""6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2"""

n=int(input("Enter number :"))
count=0
min=n
if n<4:
    print("not a composite number :")
    
else:
    for i in range(1,n+1):
       if n%i==0:
          count=count+1 
          if i>1:
              if min>i:
                 min=i
    if count>2:     
       print("Composite number")
       print("smallest factor :",min)
       print("factor count",count)  
    else:
       print("Not a composite number")   
    