"""
47Check for substring using concatenation trick. 
S1="CDAB", S2="ABCD" 
True (S1 is in S2+S2)"""
s1=input("Enter subtring :")
s2=input("Enter string :")
ispresent=False
if s1 in (s2+s2):
     ispresent=True
print(ispresent)

