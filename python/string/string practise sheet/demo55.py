"""
55Reverse only vowels.
 S = "hello" "holle"
"""
s=input("Enter the string :")
vs=""
for ch in s:
   if ch.lower() in "aeiou":
       vs+=ch
vs=vs[::-1]
j=0
for x in s:
   if x.lower() in "aeiou":
       print(vs[j],end="")
       j+=1
   else:
       print(x,end="")