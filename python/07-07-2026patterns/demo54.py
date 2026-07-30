"""
ABCDE
 A__D
  A_C
   AB
    A


"""
n=int(input("Enter number of lines :"))
i=5
while i>0:
    sp=1
    while sp<(n-(i-1)):
       print(" ",end="")
       sp=sp+1
    j=1
    while j<=i:
       if j==i or i==n or j==1:
          print(chr(j+64),end="")
       else:
          print("_",end="")
       j=j+1
    i=i-1
    print()
