"""
.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C."""

n1=int(input("Enter size of first list :"))
print("Enter elements for A list")
a=[]
for i in range(n1):
   a.append(int(input())) 
a=sorted(a)

n2=int(input("Enter size of second list :"))
print("Enter elements for B list")
b=[]
for i in range(n2):
   b.append(int(input()))
b=sorted(b)

n3=int(input("Enter size of third list :"))
print("Enter elements for C list")
c=[]
for i in range(n3):
   c.append(int(input()))
c=sorted(c)
print(*a)
print(*b)
print(*c)
l=min(n1,n2,n3)
if l==n1:
   new=a
elif l==n2:
    new=b
else:
   new=c
print()
i=0
for x in new:
    if x in a and x in b and x in c and x not in new[i+1:]:
       print(x,end=" ")
       i+=1
