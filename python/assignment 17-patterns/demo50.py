"""
12345
 1234
  123
   12
    1"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
    sp=1
    while sp<i:
       print(" ",end="")
       sp=sp+1
    j=1
    while j<=n-i+1:
       print(j,end="")
       j=j+1
    i=i+1
    print()
