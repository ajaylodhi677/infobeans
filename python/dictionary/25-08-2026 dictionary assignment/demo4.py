"""
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
"""
"""n=int(input("Enter number of studebntt :"))
d={}
max=0
min=100
for i in range(n):
    name=input("Enter student name :")
    marks=int(input("Enter marks :"))
    d[name]=marks
    if max<marks:
       max=marks
       large={}
       large[name]=marks
    if min>marks:
       min=marks
       lowest={}
       lowest[name]=marks
print("highest marks :",large)
print("Lowest marks :",lowest)
"""
n=int(input("Enter student name:"))
d={}
for i in range(n):
    name=input("Enter student name :")
    marks=int(input("Enter marks :"))
    d[name]=marks
highest=max(d.values())
low=min(d.values())
for k,v in d.items():
    if highest==v:
       print("Highest marks :",k,v)
    if low==v:
       print("Lowest marks :",k,v)
