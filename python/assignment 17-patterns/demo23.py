"""
a
bc
d f
g  j
klmno
"""
n=int(input("Enter number of lines :"))
ch=97
for i in range(1,n+1):
    for j in range(1,i+1):
       if j==1 or i==j or i==n:
          print(chr(ch),end="")
       else:
          print(" ",end ="")
       ch=ch+1
    print()

