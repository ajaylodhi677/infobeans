"""
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found"""

n=int(input("Enter size of an array :"))
arr=[]
print("enter value of list")
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
print(arr)
dup=[]
for x in arr:
   if x not in dup:
     if arr.count(x)>1:
       dup.append(x)
if len(dup)>0:
    print("duplicate number :",sorted(dup))
    print("count :",len(dup))
else:
   print("No duplicate numbers found")


