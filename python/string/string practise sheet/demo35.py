"""35Find the first palindrome word. 
S = "this madam is here" 
"madam"
"""
s=input("Enter string :").split()
for w in s:
   r=w[::-1]
   if w==r:
     print(w)
     break
else:
  print("No palindrome found")
