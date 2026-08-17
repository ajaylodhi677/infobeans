matrix=[[1,2,3],[20,25,36],[26,58,59]]

for row in matrix:
     for value in row:
         if value%2==0:
          print(value,end=" ")
         else:
          print(0,end=" ")
     print()