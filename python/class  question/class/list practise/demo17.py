"""
2. Longest Subarray With Average ≤ K
arr = [3, 1, 2, 7, 1, 4, 2]
k = 3

Find the longest contiguous subarray whose average is less than or equal to k.
"""
nums=list(map(int,input("Enter list elemets:").split()))
k=int(input("Enter average:"))
c=0
for i in range(len(nums)):
    sub=nums[:len(nums)-i]
    #print(sub)
    #print()
    for j in range(len(nums)-len(sub)+1):
        sub2=nums[j:len(sub)+j]
        if sum(sub2)/len(sub2)<=k:
            print(sub2)
            c=1
            break
    if c==1:
        break    
