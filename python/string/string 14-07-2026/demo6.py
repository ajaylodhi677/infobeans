"""
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching"""

s1=input("Enter first product code ").lower()
s2=input("Enter second product code ").lower()
s3=""
s4=""
for i in  range(len(s1)):
    ch=s1[i]
    if ch!=" ":
       s3=s3+ch
for i in  range(len(s2)):
    ch=s2[i]
    if ch!=" ":
       s4=s4+ch


if len(s3)!=len(s4):
    print("Both codes are not matching :")
else:
   i=0
   while i<len(s3):
     ch=s3[i]
     c1=0
     c2=0
     j=0
     while j<len(s3):
        if s3[j]==ch:
            c1=c1+1
        if s4[j]==ch:
            c2=c2+1
        j=j+1 
     if c1!=c2:
       print("Both codes are not matching 2")
       break
     i=i+1   
   else:
     print("Both codes are matching ") 