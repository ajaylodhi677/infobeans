"""
46Check if a substring appears at both the start and end. 
S = "abcabca", Sub="abca" TRUE
"""
s=input("Enter string :")
sub=input("Enter substring :")
print(s.startswith(sub))
print(s.endswith(sub))