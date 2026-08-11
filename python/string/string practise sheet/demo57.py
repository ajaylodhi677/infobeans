"""
57Merge two strings alternatively (char by char).
S1 = "ABC", S2 = "def" 
"AdBeCf"
"""
s1=input("Enter first string :")
s2=input("Enter second string :")
len1=min(len(s1),len(s2))
i=0
final=""
while i<len1:
      final=final+s1[i]+s2[i]
      i=i+1
if len(s1)>len(s2):
    final= final+s1[len1:]
else:
    final=final+s2[len1:]
print(final)