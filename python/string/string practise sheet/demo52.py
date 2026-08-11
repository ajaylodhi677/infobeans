"""
52Remove all special characters. 
S = "a!@b#c" "abc"
"""
s=input("Enter the string :")
s1=""
for ch in s:
   if ch.isdigit():
      s1=s1+ch
   elif ch.isalpha():
      s1+=ch
   else:
      s1=s1
print(s1)