"""
56Reverse only consonants. 
S = "apple" "eplpa"
"""
s=input("Enter the string :")
cs=""
for ch in s:
   if ch.lower()not in "aeiou":
       cs+=ch
cs=cs[::-1]
j=0
for x in s:
   if x.lower() not in "aeiou":
       print(cs[j],end="")
       j+=1
   else:
       print(x,end="")