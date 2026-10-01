mat1=[]
r1=int(input("Enter row for mat1:"))
c1=int(input("Enter column for mat1"))
for i in range(r1):
    row=[]
    print(f"Enter elements of {i+1} row")
    for j in range(c1):
        row.append(int(input()))
    mat1.append(row)  
mat2=[]
r2=int(input("Enter row for mat2:"))
c2=int(input("Enter column for mat2"))
for i in range(r2):
    row=[]
    print(f"Enter elements of {i+1} row")
    for j in range(c2):
        row.append(int(input()))
    mat2.append(row)
if r1!=r2 or c1!=c2:
    print("Addition not possible:")
else:
    result=mat1
    for i in range(r1):
        for j in range(c1):
            result[i][j]=mat1[i][j]+mat2[i][j]  
    for row in result:
        print(*row)                