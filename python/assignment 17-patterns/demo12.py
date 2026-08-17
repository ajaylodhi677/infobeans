"""
a
ab
abc
abcd
abcde"""
n=int(input("Enter number of lines :"))
for i in range(1,n+1):
    for j in range(1,i+1):
       
          print(chr(j+96), end="")
    print()
