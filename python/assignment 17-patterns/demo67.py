"""
    A
   B B
  C   C
 D     D
EEEEEEEEE



"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
     sp=n
     while sp>i:
        print(" ",end="")
        sp=sp-1
     j=1
     while j<=(2*i)-1:
        if i==n or j==1 or j==(2*i)-1 :
           print(chr(i+64),end="")
        else:
           print(" ",end="")
        j=j+1
     i=i+1
     print() 

