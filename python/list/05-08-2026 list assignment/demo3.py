"""
3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0"""
arr=list(map(int,input("Enter traffic list :").split()))
n=len(arr)
peak=[]
sum1=0

for i in  range(n):
    if i==0:
       if n==1 or arr[i]>=arr[i+1]:
          peak.append(arr[i])
          sum1+=(arr[i])**2
    elif i==n-1:
      if arr[i]>=arr[i-1]:
          peak.append(arr[i])
          sum1+=(arr[i])**2
    else:
      if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
          peak.append(arr[i])
          sum1+=(arr[i])**2
    
print("peaks :",peak)
print("sum of square :",sum1)
print("average :",sum(peak)/len(peak))
print("differncee :",(max(peak)-min(peak)))
