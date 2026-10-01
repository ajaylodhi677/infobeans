"""
3.

=========================================
WEBSITE PAGE VISIT TRACKER
==========================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time

"""
s=input("Enter page visit list :").title().split()
d={}
for x in s:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"visited ",v,"times")