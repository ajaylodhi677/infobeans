"""
43Check if two strings are rotations of each other. 
S1 = "abcde", S2 = "cdeab" 
TRUE"""
s1=input("Enter string1 :")
s2=input("Enter string2 :")
s1=s1*2
isrotate=False
if s2 in s1:
   isrotate=True
print(isrotate)
