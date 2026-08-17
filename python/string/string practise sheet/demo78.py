"""
78Find the longest mirror-image substring at both ends. 
S = "aabccbaa" "aab"
"""
"""
77Find the longest substring that appears at both ends. 
S = "abracadabra" "abra"
"""
s=input("Enter string :")
small=s[:len(s)//2]
for i in range(len(small)):
     check=small[:len(small)-i]
     checkr=check[::-1]
     if s.startswith(check) and s.endswith(checkr):
          print(check)
          break

else:
   print("No mirror image substring found")