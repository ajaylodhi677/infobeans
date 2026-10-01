"""94Find the smallest window containing all characters of another string. S1 ADOBECODEBANC", S2 = "ABC" "BANC"
"""
s1=input("Enter string 1:").upper()
s2=input("Enter string 2:").upper()
check=""
l=len(s2)
c=0
for i in range(len(s1)-len(check)):
     check=s1[:l+i]
     l1=len(check)
     for j in range(len(s1)-len(check)+1):
         check1=s1[j:l1+j] 
         for x in s2:
             if s2.count(x)<=check1.count(x):
                  break
         else:
            print(check1)
            c=1
            break
     if c==1:
        break
         