"""
44Check if two strings are anagrams.
S1 = "listen", S2 = "silent" 
TRUE"""
s1=input("Enter string 1:")
s2=input("Enter string 2:")
isan=True
if len(s2)!=len(s1):
    isan=False
else:
    vis=""
    for ch in s1:
      if ch not in vis:
       vis=vis+ch+" "
       c1=s1.count(ch)
       c2=s2.count(ch)
       if c2!=c1:
          isan=False
          break
print(isan)       