"""
41Check if a string contains a substring (without using built-in method). 
S1 = "Hello", Sub="ell" TRUE"""
s=input("Enter string :")
sub=input("Enter substring :")
isstring=False
for i in range(len(s)-len(sub)+1):
     #if sub==s[i:len(sub)+i]:
      s1=""
      for j in range(i,len(sub)+i):
        s1=s1+s[j]
      if sub==s1:
         isstring=True 
         break    
print(isstring)
    