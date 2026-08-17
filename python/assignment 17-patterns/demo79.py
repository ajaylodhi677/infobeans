"""
1
1 2
1  3
1   4
1  3
1 2
1

"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
   j=1
   while j<=i:
      if j==1 or i==j:
          print(j,end="")
      else:
          print(" ",end="")
      j=j+1
   i=i+1
   print()
i=1
while i<n:
   j=1
   while j<=n-i:
      if j==1 or j==n-i:
         print(j,end="")
      else:
         print(" ",end="")
      j=j+1
   i=i+1
   print()

        
