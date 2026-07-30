"""
123456
54321
1234
321
12
1
"""
n=int(input("Enter number of lines :"))

for i in range(n,0,-1):
    if i%2==0:
       for j in range(1,i+1):
           print(j,end="")
    else:
       for j in range(i,0,-1):
           print(j,end="")
    print()