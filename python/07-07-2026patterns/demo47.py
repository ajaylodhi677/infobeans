"""
    1
   11
  1*1
 1**1
11111

"""
n=int(input("Enter number of lines :"))

i=1
while i<=n:
     sp=n
     while sp>i:
        print(" ",end="")
        sp=sp-1
     j=1
     while j<=i:
        if i==j or i==n or j==1:
           print(1,end="")
        else:
           print("*",end="")
        j=j+1
     i=i+1
     print() 
