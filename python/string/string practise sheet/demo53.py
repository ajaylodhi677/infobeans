"""
53Remove punctuation. 
S = "Hello, world!" "Hello world"
"""
s=input("Enter the string :")
s1=""
for ch in s:
   if ch.isdigit():
      s1=s1+ch
   elif ch.isalpha():
      s1+=ch
   elif ch.isspace():
      s1+=ch
  
print(s1)