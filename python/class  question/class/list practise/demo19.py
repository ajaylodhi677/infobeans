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
if c1!=r2 :
    print("multiplication not possible:")
else:
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            row.append(0)
        result.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]=result[i][j]+mat1[i][k]*mat2[k][j]
    print("Resultant matrix:")
    for row in result:
        print(*row)