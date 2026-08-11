"""
40Search all occurrences of a word. 
S = "a b a b", 
Word='b' 
2, 6 (start indices)"""
s=input("Enter String :")
char=input("Enter character :")
for i in range(len(s)):
    if char==s[i]:
     print(i,end=" ")