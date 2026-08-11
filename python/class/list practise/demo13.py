matrix=[[1,2,3],[5,6,8],[5,9,7]]
s=int(input("Enter element you want to search :"))
for i in range(len(matrix)):
      for j in range(len(matrix[i])):
            if matrix[i][j]==s:
                 print("found element at index ",i,j)