"""
123456789
 1+++++7
  1+++5
   1+3
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
    while j<=2*i-1:
       if i==n or j==1 or j==2*i-1:
          print(j,end="")
       else:
          print("+",end="")
       j=j+1
    i=i-1
    print()

