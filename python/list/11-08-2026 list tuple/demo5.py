"""
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
"""
arr=list(map(int,input("Enter list elemnt :").split()))
pos=[]
neg=[]
for x in arr:
    if x<0:
      neg.append(x)
    else:
      pos.append(x)
l=min(len(pos),len(neg))
result=[]
for i in range(l):
    result.append(pos[i])
    result.append(neg[i])
if len(pos)<len(neg):
    result=result+neg[l:]
else:
    result=result+pos[l:]
print(arr)
print(result)