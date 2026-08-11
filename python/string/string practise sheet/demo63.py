"""
63Count frequency of each character.
S = "aabcc"
a: 2, b: 1, c: 2"""
s=input("Enter the string :")
vis=""
for ch in s:
   if ch not in vis:
       vis=vis+ch
       print(ch,":",s.count(ch))