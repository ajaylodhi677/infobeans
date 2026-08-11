"""
65Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)
"""
s=input("Enter the string :")
i=0
count=len(s)
while i<len(s):
     s1=s[i]
     j=i+1
     while j<len(s):
         s1=s1+s[j]
         v1=s1[::-1]
         if s1==v1:
            count+=1
         j+=1
     i+=1
print(count)
          

