"""
A
AB
ABC
ABCD
ABCDE
"""

n=int(input("Enter no of lines"))

for i in range(1,n+1):
    
    for j in range(65,i+65):
       print(chr(j),end="")
       n=n+1
    print()