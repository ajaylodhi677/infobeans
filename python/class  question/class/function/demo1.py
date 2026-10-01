def evenlist(n):
   even=[]
   for i in range(0,n+1,2):
       even.append(i)
   return even
result=evenlist(int(input("Ebter number :")))
print("result is :",result)