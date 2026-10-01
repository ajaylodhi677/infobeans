"""
23 
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 """
nums=list(map(int,input("Enter list elements :").split()))
k=int(input("Enter target :"))
c=0
for i in range(len(nums)):
    sum=0
    for j in range(i,len(nums)):
        sum+=nums[j]
        if sum==k:
            c+=1
print(c)