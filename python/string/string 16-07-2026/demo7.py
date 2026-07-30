"""
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.


hello hello how are are you


Output:


hello how are you"""


n=input("Enter string :")
s=""
s1=""
i=0
while i<len(n):
   ch=n[i]
   if ch !=" ":
      s=s+ch
      if ch==n[-1]:
         if s not in s1:
           s1=s1+s
   elif s not in s1:
      s1=s1+s+" "
      s=""
   else:
      s=""
   i=i+1
print(s1)