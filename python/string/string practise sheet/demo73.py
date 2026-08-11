"""
73Find the longest palindromic substring. S = "babad" "bab" (or "aba")
"""
s=input("Enter the string :")
pal=""
lens=0
for i in range(0,len(s)):
     for j in range(i+1,len(s)+1):
          sub=s[i:j]
          sub1=sub[::-1]
          if sub==sub1:
              if lens<len(sub):
                 lens=len(sub)
                 pal=sub
print(pal)
              
