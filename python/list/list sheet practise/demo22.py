"""
22 . 3 sum closseset
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""
nums=list(map(int,input("Enter list elements :").split()))
target=int(input("Enter target :"))

best=float('inf')
diff=float('inf')

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            c=nums[i]+nums[j]+nums[k]
            if abs(c-target)<diff:
                diff=abs(c-target)
                best=c

print(best)