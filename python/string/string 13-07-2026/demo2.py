"""2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
"""
n=input("Enter caht message :")
count=0
for ch in n:
    if ch ==" ":
       count=count+1
print("Total spaces :",count)