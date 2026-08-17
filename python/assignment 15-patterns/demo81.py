"""654321
    65432
     6543
      654
       65"""
n=int(input("Enter number of lines "))

for i in range(1,n):
     print()
     for s in range(1,i):
         print(" ",end="")
     for j in range(n,i-1,-1):
         print(j,end="")