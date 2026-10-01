"""
Input:
nums = [7,2,5,10,8], m = 2   (split into 2 subarrays, minimize the largest sum)

Output: 18  (split as [7,2,5] and [10,8])

Question: There's no "search space" of indices being binary-searched here — 
what is actually being binary searched, and how do you check if a 
candidate answer is "feasible" in O(n)?
"""
nums=list(map(int,input("Enter list elements:").split()))
m=int(input("Enter how many subaarys you wants:"))
if m<=len(nums)//2:
    div=len(nums)//m
    list=[]
    i=0
    k=-1
    while i<len(nums)-1:
        j=0
        l=[]
        while j<div:
            l.append(nums[k])
            #print(k)
            #print(i)
            j+=1
            i+=1
            k-=1
        list.append(l)
    if len(nums)%2==0: 
        print(list)
        print(max(list))
        print(sum(max(list)))
    else:       
        list[-1].append(nums[0])
        print(list)
        print(max(list))
        print(sum(max(list)))  
else:
    print("bhag teri maa ka bhosada")    
     
    