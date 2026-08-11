"""
72Print all substrings of length n. S = "abc", n = 2 "ab, bc"
"""
s=input("Enter the string :")
n=int(input("Input length of substring :"))
for i in range(0,len(s)):
     for j in range(i+1,len(s)+1):
          sub=s[i:j]
          if len(sub)==n:
            print(sub,end=" ")
