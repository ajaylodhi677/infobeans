"""2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System
"""
student={
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
while True:
   print("=" * 41)
   print("STUDENT MANAGEMENT SYSTEM")
   print("=" * 41)

   print("1. Add New Student")
   print("2. Search Student")
   print("3. Update Course")
   print("4. Delete Student")
   print("5. Display All Students")
   print("6. Count Total Students")
   print("7. Display Students By Course")
   print("8. Display Students By City")
   print("9. Find Student Paying Highest Fees")
   print("10. Find Student Paying Lowest Fees")
   print("11. Exit")
   choice=int(input("Enter your choice :"))
   match choice:
     case 1 :
       id=int(input("Enter student id :"))
       if id not in student:
          student[id]={"name":input("Enter name :"),
                        "course":input("Enter course :"),
                        "mobile":input("Enter mobile number :"),
                        "fees":int(input("ENter fees :")),
                        "city":input("Enter city:")
                       }
          print("Student details added succesfully")
       else:
          print("id already regiusterd")
     case 2 :
       x=int(input("Enter studenr id :"))
       if x in student:
          details=student[x]
          print("Student id :",x)
          for k,v in details.items():
             print(k.ljust(10),":",v)
       else:
         print("Student not found")
     case 3:
        x=int(input("Enter student id "))
        if x in student:
           print("old course :",student[x]["course"])
           newcourse=input("Enter new course :")
           student[x]["course"]=newcourse
           print("course updated succesfully")
        else:
           print("Student id not found :")
     case 4 :
        x=int(input("Enter student id "))
        if x in student:
             del student[x]
             print("Record deleted succesfully")
        else:
            print("Student id not found :")
     case 5 :
        print("student details :")
        for id,details in student.items():
           print("--"*10)
           print("Student id :",id)
           for k,v in details.items():
              print(k.ljust(10),":",v)
     case 6 :
        print("Total student :",len(student))
     case 7:
        fc=input("Enter course name :")
        c=0
        for id,details in student.items():
           if fc == details["course"]:
               print(id,"",details["name"])
               c=1
        if c==0:
          print("No studnet found with this course :")
     case 8 :
       fc=input("Enter city name :")
       c=0
       for id,details in student.items():
        if fc==details["city"]:
            print(id,"",details["name"])
            c=1
       if c==0:
         print("No student found with this city :")
     case 9 :
         high=0
         x=0
         for id,details in student.items():
             if details["fees"]>high:
                 high=details["fees"]
                 x=id
         print("Student paying highest fees :")
         print("Student id :",x)
         for k,v in student[x].items():
               print(k.ljust(10),":",v)
     case 10:
         low=float('inf')
         x=0
         for id,details in student.items():
             if details["fees"]<low:
                 low=details["fees"]
                 x=id
         print("Student paying lowest fees :")
         print("Student id :",x)
         for k,v in student[x].items():
               print(k.ljust(10),":",v)
     case 11:
        break
print("Thanks you for using student managemt ")