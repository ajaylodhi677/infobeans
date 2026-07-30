"""
Append two strings but remove duplicate adjacent characters. S1 = "miss", S2 = "issippi" "misisipi"""
s=input("Enter string :")
s1=input("Second chaarcter :")
s2=(s+s1).replace(" ","")
final=""
i=0
while i <len(s2):
   if i==0:
      final=s2[0]
   elif s2[i]==s2[i-1]:
       pass
   else:
       final=final+s2[i]
   i=i+1
print(final)