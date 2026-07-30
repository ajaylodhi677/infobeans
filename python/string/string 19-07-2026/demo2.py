"""2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
n=input("enter message :")+" "
w=""
vis=""
i=0
c=0
ans=""
while i<len(n):
    ch=n[i]
    if ch!=" ":
       w=w+ch
    else:
       if w not in vis:
          vis=vis+w
          j=0
          temp=""
          count=0
          while j<len(n):
              cj=n[j]
              if cj!=" ":
                 temp=temp+cj
              else:
                 if w==temp:
                    count=count+1
                    temp=""
                 else:
                    temp=""
              j=j+1       
          if count>c:
            c=count
            ans=w 
          w=""    
            
    i=i+1
print(ans)    
print(c)"""

n=input("Enter message :").split()
s=""
count=0
for ch in n:
   if n.count(ch)>count:
      count=n.count(ch)
      s=ch
   
print(count)
print(s)

