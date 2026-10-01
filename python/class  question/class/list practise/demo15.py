"""
5. Minimum Window Substring
Given strings s and t, find the smallest substring of s that contains all characters of t (with counts).
s = "ADOBECODEBANC", t = "ABC" → "BANC"
"""
s=input("Enter string:")
t=input("Enter substring:")
c=0
for i in range(len(s)-len(t)+1):
    check=s[:len(t)+i]
    #print(check)
    print()
    for j in range(len(s)-len(check)+1):
        check1=s[j:len(check)+j]
        #print(check1)
        for x in t:
            if t.count(x)>check1.count(x):
                break
        else:
            print(check1)
            c=1
            break
    if c==1:
        break
if c==0:
    print("no substring found")  