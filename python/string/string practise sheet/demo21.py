"""
21Find the first non-repeating character. 
S = "aabbcde" 
c'"""
s=input("Enter string :")
i=0
while i<len(s):
     ch=s[i]
     if s.count(ch)==1:
         print(ch)
         break
     i=i+1