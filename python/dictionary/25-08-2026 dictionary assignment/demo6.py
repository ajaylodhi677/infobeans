"""
6.

=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

"""
s=input("Enter cities :").title().split()
d={}
for x in s:
   d[x]=d.get(x,0)+1
hight=max(d.values())
for k,v in d.items():
     if hight==v:
        print("Most download :",k)