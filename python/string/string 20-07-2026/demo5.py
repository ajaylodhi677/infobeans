"""
 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca


### Explanation:

dbca contains all unique characters: a,b,c,d

---"""
s=input("Enter string :")
i=0
s1=""
while i<len(s):
    ch=s[i]
    j=i+1
    n=""
    n=n+ch
    while j<len(s):
       cj=s[j]
       if cj not in n:
         n=n+cj
       else:
         break
       j=j+1
    #print(n,end=" ")
    if len(n)>len(s1):
           s1=n
    i=i+1
print()
x=s1.split()
print(s1+" contain all unique charcter ",x)