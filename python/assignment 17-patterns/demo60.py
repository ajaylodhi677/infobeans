"""
    X 
   X X 
  X__ X
 X____ X
X X X X X



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
           print("X",end=" ")
        else:
           print("_",end="_")
        j=j+1
     i=i+1
     print() 

