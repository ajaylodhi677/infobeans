s1=input("Entr first string :")
s2=input("Enter  second string :")

if len(s1)!=len(s2) :
   print("not anagram :")
else:
   x=1
   i=0
   while i <len(s1):
      ch =s1[1]
      c1=0
      c2=0
      j=0
      while j <len(s1) :
         if s1[j]==ch :
            c1=c1+1
         j=j+1
      while j <len(s2) :
         if s2[j]==ch :
            c2=c2+1
      if c1!=c2:
         x=0
         break   
      i=i+1 
   if x==1:
      print("anagram ")
   else:
      print("not anagrams ")