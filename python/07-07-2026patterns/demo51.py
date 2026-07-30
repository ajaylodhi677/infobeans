"""
55555
 4444
  333
   22
    1
"""
n=int(input("Enter number of lines :"))
s=n
i=1
while i<=n:
    sp=1
    while sp<i:
       print(" ",end="")
       sp=sp+1
    j=1
    while j<=n-i+1:
       print(s,end="")
       j=j+1
    i=i+1
    s=s-1
    print()
