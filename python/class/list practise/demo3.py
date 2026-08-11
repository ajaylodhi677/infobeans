"""
WAP to peak element """
n=int(input("Enter size :"))
arr=[]
peakindex=-1
print("Enter element one by one :")
for k in range(n):
     arr.append(int(input()))
for i in  range(n):
    if i==0:
       if n==1 or arr[i]>=arr[i+1]:
          peakindex=i
          break
    elif i==n-1:
      if arr[i]>=arr[i-1]:
          peakindex=i
          break
    else:
      if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
          peakindex=i
          break
if peakindex!=-1:
     print("Peak index :",peakindex)
     print("value is :",arr[peakindex])
else:
     print("No peak element :")