"""WAP to print all leap year between two number"""

a=int(input("Enter number "))
b=int(input("Enter number 2nd"))


i=a
while i <=b:
#for i in range(a,b+1):
    if i%4==0:
       if i%100==0:
          if i%400==0:
              print(i,end=" ")
          else: 
       else:
          print(i,end=" ")
    else:

    i=i+1  
           