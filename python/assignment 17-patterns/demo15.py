"""
A
BB
CCC
DDDD
EEEEE"""
n=int(input("Enter number of lines :"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end="")
        
    print()

