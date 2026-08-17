"""
    A
   AB
  A_C
 A__D
ABCDE


"""
n=int(input("Enter number of lines :"))
"""
i=1
while i<=n:
     sp=n
     while sp>i:
        print(" ",end="")
        sp=sp-1
     j=1
     while j<=i:
        if i==j or i==n or j==1:
           print(chr(j+64),end="")
        else:
           print("_",end="")
        j=j+1
     i=i+1
     print() """

for i in range(1,n+1):
   for sp in range(n,i-1,-1):
      print(" ",end="")  
   for j in range(1,i+1):
      if i==j or i==n or j==1:
         print(chr(j+64),end="")
      else:
         print("_",end="")
   print()               
