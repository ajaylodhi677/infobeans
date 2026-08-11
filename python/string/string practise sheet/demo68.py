"""
count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3)
"""
s=input("Enter the string :")
sum=0
for x in s:
   if x.isdigit():
       sum+=int(x)
print(sum)