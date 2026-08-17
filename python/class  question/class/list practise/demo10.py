matrix=[[1,2,3],[5,6,8],[5,9,7]]
max=matrix[0][0]
for row in matrix:
   for v in row:
      if v>max:
         max=v
print("maximum element in matrix :",max)
