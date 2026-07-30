"""
A
AB
A C
A  D
ABCDE
"""
n=int(input("Enter number of lines :"))
for i in range(1,n+1):
    for j in range(1,i+1):
       if j==1 or i==j or i==n:
          print(chr(j+64),end="")
       else:
          print(" ",end ="")
    print()

