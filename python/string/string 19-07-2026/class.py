s=input("Enter string :")
words=s.split()
i=0
while i<len(words):
    w=words[i][::-1]
    print(w,end=" ")
    i=i+1
print()
n=input("Enter string :")
words=s.split()
for i in range(0,len(words)):
     w=words[i]
     rev=""
     for j in range(len(w)-1,-1,-1):
           rev=rev+w[j]
     print(rev,end=" ")
     