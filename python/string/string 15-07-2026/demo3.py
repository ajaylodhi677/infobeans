"""
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy"""
n=input("Enter message :")
i=0
s=""
while i<len(n):
   if n[i]!=" ":
      while i<len(n):
         ch=n[i]
         if n[i]==" " and n[i-1]==" ":
           s=s 
         else:
           s=s+ch
         i=i+1
   i=i+1  
print(s) 
