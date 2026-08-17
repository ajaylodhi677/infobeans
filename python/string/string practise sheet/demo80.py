"""
80Print list items containing all characters of a given word. 
List = ["apple", "plea"], 
Word = "pal" 
"apple", "plea"

"""
s=input("Enter list item :").split()
word=input("Enter ")
print(s)
for x in s:
    for ch in word:
        if ch not in x:
            break
    else:
       print(x,end=" ")