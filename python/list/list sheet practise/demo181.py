"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0"""

"""nums=list(map(int,input("Enter list eliment :").split()))
i=len(nums)-1
a=0
b=0
while i>0:
    x=nums[i]
    y=nums[i-1]
    if x<y:
       b=i
       break
    i-=1
c=0
j=0
while j<b-1:
   if (nums[j]>nums[j+1]) or (c==1 and nums[b]<nums[a]):
      a=j
      c=1
      break
   j+=1
if c==0 and b!=0:
  for i in range(b+1):
      if nums[b]<nums[i]:
          a=i
          break
ans=nums[a:b+1]
print(ans)
if len(ans)==1:
   print(0)
else:
   print(len(ans))"""
num = list(map(int,input("Enter elements of List:").split()))
i = 0
s = 0
e = 0
if len(num) == 1:
    print(0)
else:
    j = len(num)-1
    while j >0:
        if num[j] < num[j-1] :
            e = j
            break
        j-=1
    
    while i < j:
        if num[i] < num[i+1]:
            if num[i] > num[j]:
                s = i
                break
            else:
                i+=1
        else:
            s = i
            break
    if j == i:
        print(0)
    elif num[0] > num[-1]:
        print(len(num[:]))
    else:
        print(num[i])
        print(num[j])
        print(len(num[i:j+1]))