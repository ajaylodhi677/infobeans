"""
77Find the longest substring that appears at both ends. 
S = "abracadabra" "abra"
"""
s=input("Enter string :")
small=s[:len(s)//2]
for i in range(len(small)):
     check=small[:len(small)-i]
     if s.startswith(check) and s.endswith(check):
          print(check)
          break

else:
   print("No substring as prefix and suffix")