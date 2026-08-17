'''
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
'''


coding = set()
robotics = set()
while True:
    print()
    print("=========================================")
    print("      STUDENT CLUB MEMBERSHIP SYSTEM")
    print("=========================================")
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    match choice:

        case 1:
            cod = int(input("Enter no. of students for Coding Club: "))
            for i in range(cod):
                student = input("Enter Student name: ")
                coding.add(student)
            print("Student added to Coding Club.")

        case 2:
            rob = int(input("Enter no. of students for Robotics Club: ")) 
            for i in range(rob):
                student = input("Enter Student name: ")
                robotics.add(student)
            print("Student added to Robotics Club.")

        case 3:
            print("Coding Club Students:",coding)

        case 4:
            print("Robotics Club Students:",robotics)

        case 5:
            print("Students in Both Clubs:",coding.intersection(robotics))

        case 6:
            print("Students Only in Coding Club:",coding-robotics)

        case 7:
            print("Students Only in Robotics Club:",robotics - coding)

        case 8:
            print("All Unique Club Members:",coding.union(robotics))

        case 9:
            print("Total Unique Club Members:",len(coding|robotics))

        case 10:
            print("End of Program")
            break

        case _:
            print("Invalid choice!")