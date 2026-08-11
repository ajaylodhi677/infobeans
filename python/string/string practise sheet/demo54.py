"""
54Replace duplicate chars with '$'. 
S = "hello" 
"he$lo"
"""
s=input("Enter the string :")
vis=""
s1=""
for i in s:
    if i not in vis:
       vis+=i
       if s.count(i)>1:
          s1=s1+"$"
       else:
        s1=s1+i
    else:
        s1=s1+i
print(s1)
    
