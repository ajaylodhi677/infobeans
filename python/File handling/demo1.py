"""
1. Student Attendance Manager

A school wants to maintain the attendance of students in a text file named attendance.txt.

Each line contains:

RollNo,StudentName,Status

where Status is either Present or Absent.


Write a Python program to:

Accept attendance details for N students.
Store the details in attendance.txt.
Read the file and display:
Total students
Number of present students
Number of absent students
Attendance percentage
Sample Input
Enter number of students: 5

Enter Roll No: 101
Enter Student Name: Rahul
Enter Status: Present

Enter Roll No: 102
Enter Student Name: Priya
Enter Status: Absent

Enter Roll No: 103
Enter Student Name: Amit
Enter Status: Present

Enter Roll No: 104
Enter Student Name: Neha
Enter Status: Present

Enter Roll No: 105
Enter Student Name: Rohit
Enter Status: Absent
Expected Output
Attendance Report
-------------------------
Total Students: 5
Present Students: 3
Absent Students: 2
Attendance Percentage: 60.00%
"""   
try:
  with open("Attendance.txt","a+") as a:
     n=int(input("Enter number of students:"))
     for i in range(n):
        rollno=input("Enter roll number:")
        name=input("Enter name :")
        Status=input("Enter present status :")
        a.write(rollno+" "+name+" "+Status+"\n")
     a.seek(0)
     scount=0
     pcount=0
     for line in a:
        parts=line.split()
        r=parts[0]
        n=parts[1]
        s=parts[2]
        scount+=1
        if s.lower()=="p":
            pcount+=1
     acount=scount-pcount
     percentage=(pcount/scount)*100
     print("\n\nAttendence reports")
     print("----"*15)
     print("Total students:",scount)
     print("Present students:",pcount)
     print("Absent students:",acount)
     print("Attendance percentage:",percentage) 
except FileNotFoundError :
    print("Plaease check file name")           