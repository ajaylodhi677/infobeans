"""
x
xx
xxx
xxxx
xxx
xx
x

"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
   j=1
   while j<=i:
      print("X",end="")
      j=j+1
   i=i+1
   print()
i=n
while i>1:
   j=i
   while j>1:
      print("X",end="")
      j=j-1
   i=i-1
   print()

        
