"""
ABCDE
A  D
A C
AB
A
"""
n=int(input("Enter number of lines :"))

for i in range(n,0,-1):
    for j in range(1,i+1):
       if i==n or i==j or j==1:
          print(chr(j+64),end="")
       else:
          print(" ",end="")
    print()