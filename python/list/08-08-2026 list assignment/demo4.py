"""
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

---
"""
n=int(input("Enter size of an array :"))
arr=[]
print("enter value in increaseing order ")
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
arr=sorted(arr)
count=0
long=[]
for x in arr:
    if x not in long:
       c=1
       long.append(x)
       j=arr.index(x)+1
       while j<len(arr):
           if x+1==arr[j]:
               x=arr[j]
               c+=1
           j=j+1
       if c>count:
             count=c
print("longest consecutive length :",count)

       