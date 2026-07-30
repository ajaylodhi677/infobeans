"""
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8"""

n=input("Enter feedback message :").lower()
count=0
for ch in n:
   if  ch in "aeiou":
   #if ch =='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
       count=count+1
   
print("Total vowels :",count)