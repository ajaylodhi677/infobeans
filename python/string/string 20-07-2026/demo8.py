"""
# 8. Intelligent Search Query Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

text
Google Search


### Output:

text
a1c1e2g2h1l1o2r1s1t1"""

s=input("Enter message ").replace(" ","").lower()
s=sorted(s)
vis=[]
i=0
s1=""
while i<len(s):
    ch=s[i]
    if ch not in vis:
        vis.append(ch)
        count=s.count(ch)
        s1=s1+ch+str(count)
    i=i+1
print(s1)