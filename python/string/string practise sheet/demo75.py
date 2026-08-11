"""
75. Find the longest common prefix among strings"""
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
     check=small[:len(small)-i]
     #print(check)
     k=0
     c=0
     while k<len(word):
        if word[k].startswith(check):
        #if check in word[k]:
             #print(check)
             c=c+1
        k=k+1
     if c==len(word):
         print(check)
         break
         
     i=i+1
else:
   print("No prefix found ")