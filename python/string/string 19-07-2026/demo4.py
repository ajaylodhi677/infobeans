"""
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d"""

n=input("Enter message :")
s=""
vis=""
vis1=""
i=0
c=0
while i<len(n):
    ch=n[i]
    if ch not in vis:
        vis=vis+ch
        j=i+1
        count=0
        while j<len(n):
            if ch==n[j]:
               count=count+1 
            j=j+1
        if count>c:
           c=count
           vis1=ch
           s=ch   
    i=i+1
k=0
while k<len(n):
   ck=n[k]
   if ck not in vis1:
      vis1=vis1+ck
      l=k+1
      c1=0
      while l<len(n):
          if ck==n[l]:
              c1=c1+1
          l=l+1
      if c1==c:
        s=s+" "+ck
   k=k+1
print(s)