"""
20Find the lowest frequency character. 
S = "aabbcde" c', 'd', 'e' 
(any one or all)"""
n=input("Enter string :")
c=len(n)
i=0
s=""
vis=""
while i<len(n):
    ch=n[i]
    if ch not in vis:
      vis =vis+ch
      count=0
      j=0
      while j<len(n):
         if ch==n[j]:
            count=count+1
         j=j+1
      if count<c:
         c=count
         s=ch
    i=i+1
print(s)
