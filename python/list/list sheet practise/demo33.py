"""
33Top K Frequent Elements Medium
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
"""
nums=list(map(int,input("Enter list elements :").split()))
k=int(input("Enter k :"))
ans=[]
cvis=[]
c=[]
for x in nums:
    if x not in cvis:
      cvis.append(x)
      c.append(nums.count(x))
c.sort(reverse=True)
print(cvis)
for i in range(k):
    check=c[i]
    for x in cvis:
       if nums.count(x)==check:
          ans.append(x)
print(ans)