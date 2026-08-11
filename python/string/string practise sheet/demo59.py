"""
59Rotate characters by 3 positions to the right.
S = "abcde" "cdeab"
"""
s=input("Enter the string :")
k=int(input("Enter how many times want to rotate"))
rot=s[len(s)-k:]
s=s[:len(s)-k]
final=rot+s
print(final)

