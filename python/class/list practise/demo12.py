matrix=[[1,2,3],[5,6,8],[5,9,7]]
count=0
for row in matrix:
     for v in row:
       if v%2==0:
        count+=1
print(count)