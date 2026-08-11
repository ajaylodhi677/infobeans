"""
17Remove occurrences of a character. 
S = "banana", 
Char = 'a', 
Remove All "bnn"
"""
s=input("Enter string :")
char=input("enter charcter that you want to remove :")
s=s.replace(char,"")
print(s)