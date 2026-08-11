"""
33Find the longest word.
S = "find the longest word" 
"longest"
"""
s=input("Enter String :").split()
lc=0
l=""
vis=""
for w in s:
    if w not in vis:
       vis=vis+w+" "
       if len(w)>lc:
          lc=len(w)
          l=w
print("Longest word of string :",l)