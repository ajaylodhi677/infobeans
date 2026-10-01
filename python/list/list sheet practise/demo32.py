"""
32Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
nums=list(map(int,input("Enter list elemients:").split()))
k=int(input("Enter kth value:"))
for i in range(len(nums)):
     ch=nums[i]
     c=0
     for j in range(i+1,len(nums)):
        if ch<=nums[j]:
           c+=1
     if c==k:
       print(ch)
       break