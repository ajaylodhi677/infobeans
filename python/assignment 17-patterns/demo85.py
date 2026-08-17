"""
*         *
**       **
***     ***
****   ****
***** *****
"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
   j=1
   while j<=i:
      print("*",end="")
      j=j+1
   i=i+1
   s=1
   while s<i*2:
      print("#",end="")
      s=s+1
   print()