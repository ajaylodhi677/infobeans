"""
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
 
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
       print(i,end=" ")
       j=j+1
    i=i-1
    print()

