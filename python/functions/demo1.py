"""
1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

*** STUDENT RESULT MANAGEMENT ***

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.
"""
def ctotal(x):
    total=0
    for a in x:
        total+=a
    return total


def per(x):
    p=sum(x)/len(x)
    return p


def grade(a):
    if a>=90:
        return "A+"
    elif a>=80:
        return "A"
    elif a>=70:
        return "B"
    elif a>=60:
        return "C"
    elif a>=50:
        return "D"
    else:
        return "Fail"


def high(x):
    h=x[0]
    for a in x:
        if a>h:
            h=a
    return h


def low(x):
    l=x[0]
    for a in x:
        if a<l:
            l=a
    return l


def result(name,rno,marks):
    total=ctotal(marks)
    percentage=per(marks)
    g=grade(percentage)
    h=high(marks)
    l=low(marks)

    print("----------- RESULT CARD -----------")
    print()
    print("Name        :",name)
    print("Roll Number :",rno)
    print()
    print("Marks")

    for i in range(len(marks)):
        print("Subject",i+1,":",marks[i])

    print()
    print("Total Marks :",total)
    print("Percentage  :",percentage)
    print("Grade       :",g)
    print("Highest Mark:",h)
    print("Lowest Mark :",l)


marks=[]
name=""
rno=0

while True:
    print("--"*23)
    print("MENU")
    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Complete Result")
    print("6. Find Highest Subject Mark")
    print("7. Find Lowest Subject Mark")
    print("8. Exit")

    choice=int(input("Enter your choice :"))

    match choice:

        case 1:
            name=input("Enter student name :")
            rno=int(input("Enter rollno:"))
            marks=[]
            for i in range(5):
                while True:
                    m=int(input(f"Enter marks {i+1}:"))
                    if m>=0 and m<=100:
                        marks.append(m)
                        break
                    else:
                        print("Invalid marks. Enter marks between 0 and 100.")
            print("Student details added succesfully")
        case 2:
            if len(marks)==0:
                print("Please add student details first")
            else:
                total=ctotal(marks)
                print("Total marks :",total)
        case 3:
            if len(marks)==0:
                print("Please add student details first")
            else:
                percentage=per(marks)
                print("percentage :",percentage)
        case 4:
            if len(marks)==0:
                print("Please add student details first")
            else:
                percentage=per(marks)
                print("Grade :",grade(percentage))
        case 5:
            if len(marks)==0:
                print("Please add student details first")
            else:
                result(name,rno,marks)
        case 6:
            if len(marks)==0:
                print("Please add student details first")
            else:
                print("Highest Mark :",high(marks))
        case 7:
            if len(marks)==0:
                print("Please add student details first")
            else:
                print("Lowest Mark :",low(marks))
        case 8:
            break
        case _:
            print("Invalid choice")

print("Thanks you .progaram terminated")