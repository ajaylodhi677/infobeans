"""
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP
"""
"""s=input("Enter string : ")
s1=""
for i in range(len(s)-1,-1,-1):
   ch=s[i]
   s1=s1+ch  
print(s1) """
s=input("Enter string :").split()
i=len(s)-1
while i>=0:
   print(s[i][::-1],end=" ")
   i=i-1
