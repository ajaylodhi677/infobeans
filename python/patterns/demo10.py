"""
0
01
012
0123
01234
"""
n=int(input("Enter numbr of lines"))
i=1
for i in range(1,n+1):
    for j in range(0,i):
       print(j,end="")
    print()
