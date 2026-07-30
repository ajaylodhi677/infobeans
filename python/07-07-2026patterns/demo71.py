"""
123456789
 1234567
  12345
   123
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
       print(j,end="")
       j=j+1
    i=i-1
    print()

