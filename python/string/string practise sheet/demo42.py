"""
42Check if two strings are equal without equals(). 
S1 = "abc", S2 = "abc" 
TRUE"""
s1=input("Enter String :")
s2=input("Enter anoutheer string :")
isequal=True
if len(s1)!=len(s2):
    isequal=False
else:
   i=0
   while i<len(s1):
       if s1[i]!=s2[i]:
          isequal=False
          break
       i=i+1
print(isequal)
