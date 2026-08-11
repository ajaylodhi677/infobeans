"""
32Count frequency of each word. 
S = "apple banana apple" 
apple: 2, banana: 1"""
s=input("Enter String :").split()
vis=""
for w in s:
    if w not in vis:
       vis=vis+w+""
       print(w,":",s.count(w)) 