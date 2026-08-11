"""
Remove 'b' and 'ac' from a string. 
S = "abacbb" 
"c" """
s=input("Enter string :")+" "
result=""
i=0
while i<len(s)-1:
    ch=s[i]
    if ch=="b"  :
       pass
    elif  ch=="a" and s[i+1]=="c":
       pass
       i=i+1
    else:
       result=result+ch
    i=i+1
print(result)
