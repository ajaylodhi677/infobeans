"""
10 return zero
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
nums=list(map(int,input("Enter list elements :").split()))
#for i in range(len(nums)):
for x in nums:
   # x=nums[i]
    if x==0:
      nums.remove(x)
      #nums.append(x)
print(nums)