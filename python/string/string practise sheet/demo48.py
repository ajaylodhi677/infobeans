"""
48Remove all vowels. 
S = "aeiou XYZ" 
" XYZ"
"""
s=input("Enter the string :")
s2=""
for ch in s:
     if ch.lower() not in "aeiou":
        s2=s2+ch
print(s2)