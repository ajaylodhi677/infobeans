"""
23Print all characters that occur exactly twice. 
S = "aabbcdee" 
b', 'e'"""

s=input("Enter string :")
vis=""
for ch in s:
   if ch not in vis:
       vis=vis+ch
       count=s.count(ch)
       if count==2:
          print(ch,end=" ")