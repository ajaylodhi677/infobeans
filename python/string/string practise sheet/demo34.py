"""
34Find the shortest word. 
S = "find the shortest word" 3
"the"
"""
s=input("Enter the string :").split()
sl=s[0]
sc=len(s)
vis=[]
for w in s:
   if w not in vis:
       vis.append(w)
       if len(w)<sc:
          sc=len(w)
          sl=w
print("shortest word :",sl)
