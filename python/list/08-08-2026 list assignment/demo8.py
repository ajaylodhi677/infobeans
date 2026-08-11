"""
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found

---

===================================================================="""
n=int(input("Enter size of an array :"))
arr=[]
print("enter value of list")
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
c=n//2
print(c)
for x in arr:
    if arr.count(x)>c:
       print("majority element :",x)
       break
else:
   print("No majority element found :")