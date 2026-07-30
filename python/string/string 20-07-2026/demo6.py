"""
# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

text
Spam Pattern Found


Else:

text
Clean Message


### Input:

text
heyyy broooo welcome


### Output:

text
Spam Pattern Found"""
s=input("Enter message :")
pre=""
i=0
while i<len(s):
    pre=s[i]
    if i<len(s)-2:
       j=i+1
       c=0
       while j<i+3:
          if s[j]==pre:
              c=c+1
          j=j+1
       if c==2:
          print("Spam pattern found :")
          break
    i=i+1
else:
   print("Clean message ")