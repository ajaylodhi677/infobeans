"""
Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B
"""
class Student:
    def __init__(self):
        self.roll_number=int(input("Enter Roll number:"))
        self.student_name=input("Enter Student name:")
        self.subject1=int(input("Enter marks in subject1:"))
        self.subject2=int(input("Enter marks in subject2:"))
        self.subject3=int(input("Enter marks in subject3:"))
    def calculations(self):
        self.total_marks=self.subject1+self.subject2+self.subject3
        self.percentage=self.total_marks/3
        a=self.percentage
        if a >=90:
            self.Grade="A"
        elif a>=75:
            self.Grade="B"
        elif a>=60:
            self.Grade="C"
        else:
            self.Grade="D"
    def display(self):
        print("------Student details------") 
        print("Roll number".ljust(20),":",self.roll_number)
        print("Student name".ljust(20),":",self.student_name)
        print("Total marks".ljust(20),":",self.total_marks)
        print("percentage".ljust(20),":",self.percentage)
        print("Grade".ljust(20),":",self.Grade) 
s1=Student()
s1.calculations()
s1.display()                      
                       
                    

