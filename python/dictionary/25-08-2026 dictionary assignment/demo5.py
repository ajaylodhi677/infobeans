"""
5.

=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}

"""
s=input("Enter programming langusges :").split()
d={}
for x in sorted(s,key=len):
    length=len(x)
    if length not in d:
       d[length]=[]
    d[length].append(x)
print(d)