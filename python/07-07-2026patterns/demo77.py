"""
1
12
123
1234
123
12
1

"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
   j=1
   while j<=i:
      print(j,end="")
      j=j+1
   i=i+1
   print()
i=n
while i>1:
   j=1
   while j<i:
      print(j,end="")
      j=j+1
   i=i-1
   print()

        
