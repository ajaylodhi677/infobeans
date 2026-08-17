
'''
2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
'''


python = set()
java = set()
while True:
    print()
    print("=========================================")
    print("     ONLINE COURSE ENROLLMENT SYSTEM")
    print("=========================================")
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    match choice:

        case 1:
            pyth = int(input("Enter no. of students enrolling for Python: "))
            for i in range(pyth):
                student = input("Enter Student name: ")
                python.add(student)
            print("Student enrolled for python.")

        case 2:
            jav = int(input("Enter no. of students enrolling for Java: ")) 
            for i in range(jav):
                student = input("Enter Student name: ")
                java.add(student)
            print("Student enrolled for java.")

        case 3:
            print("Python Students:",python)

        case 4:
            print("Java Students:",java)

        case 5:
            print("Students enrolled in both cources:",python.intersection(java))

        case 6:
            print("Students enrolled only in python:",python-java)

        case 7:
            print("Students enrolled only in java:",java- python)

        case 8:
            student_name = input("Enter student name to check enrollment in python: ")
            if student_name in python:
                print("Student enrolled for python")
            else: 
                print("Student is not enrolled for python")

        case 9:
            print("Total Unique student:",len(java|python))

        case 10:
            print("End of Program")
            break

        case _:
            print("Invalid choice!")