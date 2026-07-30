"""
a
ab
abc
abcd
abcde
"""

n=int(input("Enter no of lines"))

for i in range(1,n+1):
    
    for j in range(97,i+97):
       print(chr(j),end="")
       n=n+1
    print()