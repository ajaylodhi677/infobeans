"""
A
BCD
EFGHI
JKLMNOP


"""
n=int(input("Enter number of lines :"))
i=1
k=0
s=1
while i<=n:
   j=1
   while j<=i+k:
      print(chr(s+64),end="")
      j=j+1
      s=s+1
   i=i+1
   k=k+1
   print()
