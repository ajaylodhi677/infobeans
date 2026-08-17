"""
79Divide a string into n equal parts. 
S = "abcdef", n = 3 
"ab", "cd", "ef"
"""
s=input("Enter String containg even lenth:")
n=int(input("Enter hiw many times you want to split"))
l=len(s)//n
s1=""
for ch in s:
    s1+=ch
    if len(s1)==l:
       print(s1,end=" ")
       s1=""
print(s1)