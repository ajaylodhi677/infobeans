s=list(map(int,input("Enter lsit element :").split()))
count=0
k=int(input("Enter target :"))
for i in range(len(s)):
     for j in range(i+1,len(s)):
          if s[i]+s[j]==k:
             count+=1
print(count)