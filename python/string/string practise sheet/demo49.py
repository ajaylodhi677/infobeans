"""
49Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple" "ap*le" (or similar output depending on implementation)"""
s=input("Enter String :")
s1=""
for ch in s:
   if ch.lower() not in "aeiou":
       s1=s1+"*"
   else:
       s1=s1+ch
print(s1)
      