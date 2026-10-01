"""
25
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]"""
nums=list(map(int,input("Enter lsit elements :").split()))
k=int(input("Enter target :"))
i=0
j=len(nums)-1
res=[-1,-1]
while i<len(nums):
    if nums[i]==k and res[0]==-1:
          res[0]=i
    if nums[j]==k and res[1]==-1:
          res[1]=j
    i+=1
    j-=1
print(res)