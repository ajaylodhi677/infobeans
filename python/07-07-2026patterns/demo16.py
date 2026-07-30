"""
a
bc
def
ghij
klmno
"""
n=int(input("Enter number of lines :"))
ch=97
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch=ch+1
    print()
