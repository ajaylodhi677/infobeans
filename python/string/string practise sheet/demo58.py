"""
58Rotate characters by 2 positions to the left.
S = "abcde" "cdeab"
"""
s=input("Enter the string :")
k=int(input("Enter how many times want to rotate"))
rot=""
i=0
final=""
while i <k:
    rot+=s[i]
    i=i+1
s=s[k:]
final=s+rot
print(final)