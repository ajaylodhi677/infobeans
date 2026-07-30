"""3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times"""

n=input("Enter product review :").lower()
oc=input("ENter character to check :").lower()
count=0
for ch in n:
    if ch==oc:
       count=count+1
print("Character ",oc,"occurs :",count,"times")