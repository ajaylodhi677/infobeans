"""
31Remove duplicate words. 
S = "the cat and the dog" 
"the cat and dog" """

s=input("Enter string :").split()
s1=""
for w in s:
   if w not in s1:
       s1=s1+w+" "
print(s1)      