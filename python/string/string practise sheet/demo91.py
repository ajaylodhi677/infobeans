"""
91Check if two strings are interleaving of another string. S1 = "aab", S2 = "axy", S3 = "aaxaby" TRUE
"""
s=input("Enter string1 :")
s1=input("Enter string2 :")
s2=input("Enter string 3")
l=len(s1)+len(s)
a=[]
a1=[]
if len(s2)!=l:
   print("False")
else:
  for x in s:
     for i in range(len(s2)):
         if x==s2[i] and i not in a:
            a.append(i)
            break
  for x in s1:
      for i in range(len(s2)):
        if x==s2[i] and i not in a1 and i not in a:
          a1.append(i)
          break
print(a)
print(a1)