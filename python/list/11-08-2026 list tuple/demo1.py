"""
1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)

"""
n=int(input("Enter size of an array:"))
ages=[]
for i in range(n):
     ages.append(int(input(f"Enter age of {i+1} employee :")))
print(ages)
k=int(input("enter value of k :"))
i=0
kcount=0
while i<n:
    x=ages[i]
    j=i+1
    while j<n:
         if abs(x-ages[j])==k:
             kcount+=1
         j+=1
    i+=1
print(kcount)