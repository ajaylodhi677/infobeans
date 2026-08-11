"""
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

---

====================================================================
"""
n=int(input("Enter size of an array :"))
arr=[]
print("enter value in increaseing order ")
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
print(arr)
for i in range(1,len(arr)-1):
      lsum=sum(arr[:i])
      rsum=sum(arr[i+1:])
      if lsum==rsum:
         print("Equlibrium index :",i)
         break
else:
   print("No equlibrium index found")
