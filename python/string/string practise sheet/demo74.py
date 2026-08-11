"""
74Find the longest substring without repeating characters. 
S = "abcabcbb" "abc"
"""
s=input("enter String :")
long=""
longc=0
i=0
while i<len(s):
     ch=s[i]
     s1=ch
     j=i+1
     while j<len(s):
         cj=s[j]
         if cj not in s1:
             s1+=cj
         else:
             break
         j+=1
     i+=1
     if longc<len(s1):
         longc=len(s1)
         long=s1
print(long)         
