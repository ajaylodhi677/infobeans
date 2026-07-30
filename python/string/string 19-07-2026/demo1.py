# 1.
# Find the Longest Substring Without Repeating Characters
# Cybersecurity Session Tracking System

# A cybersecurity company monitors user session IDs generated during secure login sessions.

# To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

# Input:
# abcabcbb
# Output:
# abc

n=input("Enter String :")
s=""
s1=""
i=0
while i<len(n):
    ch=n[i]
    j=i+1
    s=ch
    #print(0)
    while j<len(n):
        if n[j] not in s:
              s=s+n[j]
              j=j+1  
        else:
            break    
    if len(s)>len(s1) :
        s1=s   
    i=i+1
print(s1)    