"""
A B C D E
 A B C D
  A B C
  A B
   A
 
"""
n=int(input("Enter number of lines :"))
i=n
while i>0:
    sp=1
    while sp<(n-(i-1)):
       print(" ",end="")
       sp=sp+1
    j=1
    while j<=i:
       print(chr(j+64),end=" ")
       j=j+1
    i=i-1
    print()

