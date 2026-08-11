"""
62Count vowels and consonants. 
S = "apple" 
Vowels: 2, Consonants: 3"""
s=input("enter string :")
vc=0
cc=0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vc+=1
        else:
            cc+=1
print("vowels :",vc,"consonants :",cc)