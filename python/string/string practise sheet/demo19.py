"""
19Find the highest frequency character.
S = "abracadabra" 
a'
"""
n=input("Enter string :")
c=0
vis=""
s=""
i=0
while i<len(n):
    ch=n[i]
    if ch not in vis:
       vis=vis+ch
       count=n.count(ch)
       if count>c:
         c=count
         s=ch
    i=i+1
print(s)