"""
. Add Two Binary Strings

Given two binary strings, find their sum and return the result as a binary string.

Problem Statement:

Given two binary strings a and b, add the two binary numbers and return their sum in the form of a binary string.

Example 1:

Input:

a = "11"
b = "1"

Output:

"100"

Explanation:

  11
+ 01
----
 100

Example 2:

Input:

a = "1010"
b = "1011"

Output:

"10101"

Explanation:

  1010
+ 1011
------
 10101

Constraints:

1 <= a.length, b.length <= 10⁴
a and b contain only '0' and '1'.
Neither string contains leading zeros except "0".
"""
'''
6
Add Binary
Input: a = "11", b = "1"
Output: "100"
'''
a = input("Enter 1st binary number: ")
b = input("Enter 2nd binary number: ")
result= int(a,2) + int(b,2)
print("sums is: ", bin(result)[2:])
