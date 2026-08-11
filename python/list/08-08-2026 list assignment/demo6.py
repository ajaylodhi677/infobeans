"""
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]

---

===================================================================="""
n=int(input("Enter size of an array :"))
arr=[]
print("enter value of list")
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
print(arr)
prod=[]
i=0
while i<len(arr):
      j=0
      pro=1
      while j<len(arr):
         if j!=i:
           pro=pro*arr[j]
         j+=1
      i+=1
      prod.append(pro)
print(prod)