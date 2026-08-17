"""
    A
   A B
  A B C
 A B C D
A B C D E  


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
        print(chr(j+64),end=" ")
        j=j+1
     i=i+1
     print() 

