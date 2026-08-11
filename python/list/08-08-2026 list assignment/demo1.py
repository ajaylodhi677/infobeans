"""
1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found

---

===================================================================="""
n=int(input("Enter size of an array :"))
arr=[]
for i in range(n):
   print("element :",i+1)
   arr.append(int(input()))
print(arr)
count=0
for x in arr:
    if arr.count(x)==1:
        print("first non repeating number=",x)
        break
else:
   print("No non repeating number found")
