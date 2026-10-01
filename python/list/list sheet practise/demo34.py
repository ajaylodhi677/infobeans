"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 """
nums=list(map(int,input("Enter list elements:").split()))
result=[]
for i in range(len(nums)):
    p1=nums[:i]
    p2=nums[i+1:]
    comp=p1+p2
    pro=1
    for x in comp:
        pro*=x
    result.append(pro)
print(result)    