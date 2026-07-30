"""
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:


iphone


Output:


2"""

n=input("Enter semtence :")
w=input("Enter word :")
count=0
i=0

while i<=len(n)-len(w):
    s=""
    j=i
    while j<=len(w)+i-1:
       ch=n[j]
       s=s+ch
       j=j+1
    i=i+1
    #clsprint(s,end="")
    if w==s:
       count=count+1
"""s=""
while i <len(n):
    ch=n[i]
    if ch!=" ":
      s=s+ch
    elif w==s:
      s=""
      count=count+1
    else:
      s=""
    i=i+1  """
print(count)
