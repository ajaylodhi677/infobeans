"""8.
Online Exam Result Processing System

An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277"""

cs=int(input("Enter number of classes :"))
student=int(input("Enter student per classes :"))
subject=int(input("Enter subject per classes :"))

for c in range(1,cs+1):
    print("class ",c)
    for s in range(1,student+1):
       print("Student ",s)
       total=0
        
       for j in range(1,subject+1):
           a=int(input("Enter marks :"))
           total =total+a
           
       print("class:",c)
       print("student :",s, "Total ",total,"\n")