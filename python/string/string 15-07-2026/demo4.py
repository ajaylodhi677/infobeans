"""
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop"""
n=input("Enter message :")
i=0
s1=""
i=0
s=""
while i<len(n):
    ch=n[i]
    if ch!=" " and i!=len(n)-1:
       s=s+ch
    elif i==len(n)-1:
       s=s+n[-1] 
       for j in range(len(s)-1,-1,-1):
          s1=s1+s[j]
       s=""
    else:
       for j in range(len(s)-1,-1,-1):
          s1=s1+s[j]
       s1=s1+" "
       s=""

    i=i+1 
print(s1)    