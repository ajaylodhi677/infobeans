"""
Assignment 1: Student Result Calculator

 A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%
"""
class Student: 
    def Calculate(self):
        self.name=input("Enter name:")
        self.rno=int(input("Enter roll no:"))
        self.english=int(input("Enter english marks:"))
        self.maths=int(input("Enter maths marks:"))
        self.science=int(input("Enter science marks:"))
        self.total=self.english+self.maths+self.science
    def percentage(self):
        self.per=self.total/3
    def display(self):
        print("Student name:",self.name)
        print("Roll number:",self.rno)        
        print("Total marks:",self.total)        
        print("Percentage:",self.per)    
s1=Student()
s1.Calculate()
s1.percentage()
s1.display() 
s2=Student()           
s2.Calculate()
s2.percentage()
s2.display() 
