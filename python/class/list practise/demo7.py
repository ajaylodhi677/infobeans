s=list(map(int,input("Enter lsit element :").split()))
k=int(input("Enter how many times rotate :"))
print(s)
s1=[]
final=[]
if k>
for i in range(k):
     last=s.pop(-1)
     s1.insert(0,last)
final=s1+s
print(final)

   