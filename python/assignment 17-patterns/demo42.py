"""
54321
5432
543
54
5
"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
   j=n
   while j>=i:
      print(j,end="")
      j=j-1
   i=i+1
   print()