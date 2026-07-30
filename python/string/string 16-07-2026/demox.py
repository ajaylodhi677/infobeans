n=input("Enter string ")
s=""
i=0
while i<len(n):
   c=0
   ch=n[i]
   j=i+1
   while j<len(n):
      cj=n[j]
      if ch==cj:
         c=1
         break
      j=j+1
   if c==0:
      print(ch,end=" ")
   i=i+1