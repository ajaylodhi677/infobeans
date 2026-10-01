"""
95Find the second most frequent character. S = "aabbccdde" c' or 'd'
"""
s=input("Enter the string :")
s=list(s)
max=0
ms=""
m2=0
ms2=""
for x in s:
    a=s.count(x)
    if a>max:
        max=a
        ms=x
    if m2<max and m2<a:
        m=max
        ms2=ms
print(ms2)
         