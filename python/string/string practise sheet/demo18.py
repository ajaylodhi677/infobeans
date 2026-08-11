"""
18Replace occurrences of a character. 
S = "apple", 
Old='p', 
New='x' 
"axxle"
"""
s=input("enter string :")
old=input("which charcter  you want to replace :")
new=input("enter character to replace with :")
s=s.replace(old,new)
print(s)