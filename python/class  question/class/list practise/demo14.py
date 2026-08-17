m1=[[1,2,3],[5,6,8],[5,9,7]]
m2=[[2,3,5],[6,2,4]]
result=[]
if len(m1)==len(m2):
    
    for i in range(len(m1)):
        if len(m1[i])==len(m2[i]):
           row=[]
           for j in range(len(m1[i])):
              row.append(m1[i][j]+m2[i][j])

           result.append(row)
        else:
           print("differen column size ")
           break
    else:
      print("display result :")
      print(result)
else:
   print("row size different :")
         
     