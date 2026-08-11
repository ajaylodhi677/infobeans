"""
39Search all occurrences of a character.
 S = "banana", Char='a' 
1, 3, 5 (indices)"""
s=input("Enter String :")
char=input("Enter character :")
for i in range(len(s)):
    if char==s[i]:
     print(i,end=" ")