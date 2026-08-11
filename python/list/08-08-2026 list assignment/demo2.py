"""
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

---
===================================================================="""
n=int(input("Enter size of an array :"))
arr=[]
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
print(arr)
count=0
for x in arr:
    if arr.count(x)>1:
        print("first repeating number=",x)
        break
else:
   print("No repeating number found")
