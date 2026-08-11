"""
64Count frequency of each vowel. 
S = "programming" o: 1, a: 1 (e, i, u: 0)
"""
s=input("Enter the string :")
vis=""
for ch in s:
    if ch.lower() in "aeiou":
       if ch not in vis:
           vis+=ch
           print(ch,":",s.count(ch))
        
