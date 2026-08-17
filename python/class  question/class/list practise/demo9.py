rows=int(input("Enter size of rows :"))
cols=int(input("Enter size of column :"))
matrix=[]
print("Enter element of matrix :")
sum1=0
for i in range(rows):
      row=[]
      for j in range(cols):
          x=int(input())
          sum1+=x
          row.append(x)
      matrix.append(row)
print(sum1)
print("Print matrix element :")
sum=0
for row in matrix:
     for value in row:
       print(value,end=" ")
       sum+=value
     print()
print(sum)

