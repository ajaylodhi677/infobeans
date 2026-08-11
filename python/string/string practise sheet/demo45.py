"""
45Check whether a string starts/ends with another string. 
S = "apple pie", Prefix = "apple", Suffix = "pie" 
Start: True, End: True """

s=input("Enter the string:")
pre=input("Enter the prefix :")
suf=input("Enter the suffix :")
print(s.startswith(pre))
print(s.endswith(suf))
"""issuffix=False
ispre=False
if s.startswith(pre):
    ispre=True
if s.endswith(suf):
    issuffix=True
print("Start ",ispre)
print("End ",issuffix)"""