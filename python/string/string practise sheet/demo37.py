"""
37Reverse each word. 
S = "cat dog" 
"tac god"
"""
s=input("Enter the string :").split()
rev=""
for i in s:
    rev=rev+i[::-1]+" "
print(rev)