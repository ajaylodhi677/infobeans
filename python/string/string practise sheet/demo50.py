"""
50Remove all digits. 
S = "a1b2c3" 
"abc"
"""
s=input("Enter the string :")
s1=""
for ch in s:
   if ch.isdigit() :
      s1=s1
   else:
      s1+=ch
print(s1)
   