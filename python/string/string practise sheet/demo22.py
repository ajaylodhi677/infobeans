"""
22Find the least repeating character. 
S = "abracadabra" 
r'"""

s=input("Enter string :")
s=sorted(s)
lc=len(s)
vis=[]
ls=""
for x in s:
   if x not in vis:
      vis.append(x)
      count=s.count(x)
      if lc>count:
         lc=count
         ls=x
print("least repeating chaacter :",ls)