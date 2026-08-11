"""
3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3

---

====================================================================
"""
n=int(input("Enter size of an array :"))
arr=[]
print("enter value in increaseing order ")
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
print(arr)
miss=[]
"""i=0
c=0
s=0
while i<n-1:
    if c==0 and i==0 and arr[0]!=1:
       j=1
       x=arr[0]
       c=1
    else:
       j=arr[i]+1
       x=arr[i+1]
    #print("aatemot",i,"and j=",j,"andx=",x)
    while j<x:
       miss.append(j)
       j+=1
    if c==1 and i==0 and s==0:
       i-=1
       s=1
    i+=1"""
i=1
while i<n+1:
    if i not in arr:
       miss.append(i)
    i+=1
print(miss)
   