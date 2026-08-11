"""
10Trim leading, trailing, or extra spaces. 
S = "  hello  world  " 
"hello world" """

s=input("Enter string :").split()
s=" ".join(s)
print(s)
