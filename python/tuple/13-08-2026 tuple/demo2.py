"""QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
"""
from collections import namedtuple
student=namedtuple("Student",["rollno","name","course","marks"])
n=int(input("Enter number of students :"))
stu=[]
for i in range(n):
    print("Enter details for sudent :",i+1)
    rollno=int(input("Enter roll no :"))
    name=input("Enter stident name :")
    course=input("Enter couser name :")
    marks =int(input("Enter marks :"))
    stu.append(student(rollno,name,course,marks))
print("==="*20)
print("showing details")
cfind=input("Which course studnt you want to filter :").lower()
top=stu[0]
c=0
total=0
cf=[]
for x in stu:
    print(x.rollno,x.name,x.course,x.marks)
    if x.marks>top.marks:
        top=x
    if x.marks>80:
       c+=1
    if (x.course).lower()==cfind:
      cf.append(x)
    total+=x.marks
print("==="*20)
print("Topper ")
print(top.rollno,top.name,top.course,top.marks)
print("==="*20)
print("Students above 80")
print(c)
print("==="*20)
print("average marks")
print(total/n)
print("==="*20)
print("Studen with couser :",cfind)
for x in cf:
   print(x.rollno,x.name,x.course,x.marks)
