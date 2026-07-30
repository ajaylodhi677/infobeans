"""
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5"""

c=input("Enter complaint :")
count=0
i=0
while i<len(c):
    if c[i]!=" ":
       count+=1
       while i<len(c) and c[i]!=" ":
           i=i+1
    else:
       i=i+1
print("Total words ",count) 