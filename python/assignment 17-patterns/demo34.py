"""
EEEEE
DDDD
CCC
BB
A
"""
n=int(input("Enter number of lines :"))

for i in range(n,0,-1):
    for j in range(1,i+1):
       print(chr(i+64),end="")
    print()