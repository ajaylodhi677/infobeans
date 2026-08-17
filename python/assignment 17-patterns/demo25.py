"""
5
54
543
5432
54321"""

n=int(input("{Enter number of lines :"))

for i in range(n,0,-1):
     for j in range(n,i-1,-1):
        print(j,end="")
     print()
    