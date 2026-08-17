"""
1
222
33333
4444444
555555555"""
n=int(input("Enter number of lines :"))
i=1
k=0
while i<=n:
   j=1
   while j<=i+k:
      print(i,end="")
      j=j+1
   i=i+1
   k=k+1
   print()

