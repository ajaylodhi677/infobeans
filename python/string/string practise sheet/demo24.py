"""
24Check if all characters in a string are unique. 
S1 = "abc", 
S2 = "abca" 
S1: True, S2: False"""

s=input("Enter String :")
isunique=True
for ch in s:
    if s.count(ch)>1:
        isunique=False
        break
print("Unique string :"isunique)