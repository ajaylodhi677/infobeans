"""
90Remove adjacent duplicates recursively. S = "azxxzy" "ay"
"""
s=input("Enter string :")+" "
s1=""
x=True
while x:
  i=0
  while i<(len(s)-1):
       if s[i]==s[i+1]:
          i+=1  
       else:
         s1=s1+s[i]
       i+=1
  s=s1+" "
  s1=""
  for j in range(len(s)-1):
     if s[j]==s[j+1]:
        break
  else:
    x=False
print(s)