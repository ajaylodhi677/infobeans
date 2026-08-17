"""
1
123
12345
1234567
123456789
"""
n=int(input("Enter number of lines :"))
i=1
k=0
while i<=n:
   j=1
   while j<=i+k:
      print(j,end="")
      j=j+1
   i=i+1
   k=k+1
   print()
