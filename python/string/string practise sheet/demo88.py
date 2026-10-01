"""
88Rearrange a string so that identical characters are at least d distance apart. S = "aaabc", d = 2 "abaca"
"""
s=input("Enter string :")+" "
id=""
id1=""
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
       id=id+s[i]
    else:
       id1=id1+s[i]
print(id)
print(id1)

if len(id)>len(id1):
   l=len(id)
else:
   l=len(id1)
for i in range(l):
     