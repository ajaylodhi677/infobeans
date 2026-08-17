"""
76Find the longest common suffix among strings. 
Strings = ["baking", "making", "taking"] 
"king"
"""
s=input("Enter string :")
word=s.split()
small=s
i=0
while i<len(word):
     if len(small)>len(word[i]):
          small=word[i]
     i=i+1
i=0
while i<len(small):
     check=small[i:]
     #print(check)
     k=0
     c=0
     while k<len(word):
        if word[k].endswith(check):
        #if check in word[k]:
             #print(check)
             c=c+1
        k=k+1
     if c==len(word):
         print(check)
         break
         
     i=i+1
else:
   print("No suffix found ")