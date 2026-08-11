"""81Generate a hash code or UUID. 
input S = "test"  
output Hash: 3556498 (Example hash code)"""
s=input("Enter string :")
ans=0
for ch in s:
    ans = 31 * ans + ord(ch);
print(ans)