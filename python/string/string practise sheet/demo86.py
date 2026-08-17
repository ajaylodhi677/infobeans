"""
86Print all permutations of a string without repetition. 
S = "ab" 
"ab", "ba"
"""
s=input("Enter string :")
i=0
result=""
while i<len(s):
     ch=s[i]
     j=0
     s1=ch
     while j<len(s):
        if i!=j:
          s1+=s[j]
        j+=1
     k=len(s)-1
     s2=ch
     while k>=0:
        if i!=k:
          s2+=s[k]
        k-=1
     i+=1
     if s1 not in result:
          result+=s1+" "
     if s2 not in result:
          result+=s2+" "
print(result)     