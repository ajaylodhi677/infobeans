"""
ASSIGNMENT 1: STUDENT MANAGEMENT SYSTEM
=======================================

-------
A coaching institute wants to manage student records using
Python Database Connectivity (PDBC).

TABLE STRUCTURE
===============

Table Name: student_pdbc

Column       Data Type
--------------------------------
sid          INT PRIMARY KEY
sname        VARCHAR(50)
course       VARCHAR(50)
fees         DECIMAL(10,2)
city         VARCHAR(30)


SAMPLE DATA
===========

sid   sname    course    fees       city
------------------------------------------------
101   Amit     Python    15000.00   Indore
102   Priya    Java      18000.00   Bhopal
103   Rahul    Python    15000.00   Indore
104   Neha     Java      18000.00   Ujjain
105   Karan    MERN      20000.00   Indore


MENU
====

===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student by Name
4. Update Student Fees
5. Delete Student
6. Exit

Enter your choice:


TASK 1: ADD STUDENT
===================

INPUT
-----
Enter your choice: 1
Enter Student ID: 106
Enter Student Name: Anjali
Enter Course: Python
Enter Fees: 15000
Enter City: Dewas

OUTPUT
------
Student inserted successfully.


TASK 2: DISPLAY ALL STUDENTS
============================

INPUT
-----
Enter your choice: 2

OUTPUT
------
ID    Name      Course    Fees       City
------------------------------------------------
101   Amit      Python    15000.00   Indore
102   Priya     Java      18000.00   Bhopal
103   Rahul     Python    15000.00   Indore
104   Neha      Java      18000.00   Ujjain
105   Karan     MERN      20000.00   Indore
106   Anjali    Python    15000.00   Dewas


TASK 3: SEARCH STUDENT BY NAME USING LIKE
=========================================

INPUT
-----
Enter your choice: 3
Enter name to search: an

OUTPUT
------
Matching students:

ID    Name      Course    Fees       City
------------------------------------------------
105   Karan     MERN      20000.00   Indore
106   Anjali    Python    15000.00   Dewas

NOTE
----
Use a parameterized query with:
WHERE sname LIKE %s

Pass the search pattern:
'%' + search_name + '%'


TASK 4: UPDATE STUDENT FEES
===========================

INPUT
-----
Enter your choice: 4
Enter Student ID: 101
Enter New Fees: 17000

OUTPUT
------
Student fees updated successfully.


TASK 5: DELETE STUDENT
======================

INPUT
-----
Enter your choice: 5
Enter Student ID: 104

OUTPUT
------
Student deleted successfully.


TASK 6: EXIT
============

INPUT
-----
Enter your choice: 6

OUTPUT
------
Thank you for using Student Management System.


=
"""
import mysql.connector
print("connected succesfully")

conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="pdbc13_11_2026"
)
cursor=conn.cursor()
#cursor.execute("create table student_pdbc (sid int primary key,sname varchar(30),course varchar(30),fees decimal(10,2),city varchar(30))")

#cursor.execute("desc student_pdbc")
#res=cursor.fetchall()
#print(res)
"""n=int(input("Enter number of student:"))
data=[]
for i in range(n):
    print(f"Enter details for {i+1} student")
    sid=int(input("enter student id:"))
    sname=input("Enter student name:")
    course=input("Enter course:")
    fees=float(input("enter fees:"))
    city=input("enter city:")
    data.append((sid,sname,course,fees,city))
query="insert into student_pdbc values(%s,%s,%s,%s,%s)"

cursor.executemany(query,data)
conn.commit()
print("data inserted succesfully")
"""

def addStudent(data):
    query="insert into student_pdbc values(%s,%s,%s,%s,%s)"
    cursor.execute(query,data)
    conn.commit()
    print("student added succesfully")
def Display():
    cursor.execute("select * from student_pdbc")
    res=cursor.fetchall()
    print("Student ID".ljust(12), "Name".ljust(15), "Course".ljust(15), "Fees".ljust(12), "City".ljust(15))
    for row in res:
        print(str(row[0]).ljust(12), str(row[1]).ljust(15), str(row[2]).ljust(15), str(row[3]).ljust(12), str(row[4]).ljust(15))  

def search(name):
    q=("select * from student_pdbc where sname like %s") 
    cursor.execute(q,('%'+name+'%',)) 
    res=cursor.fetchall()
    print("Student ID".ljust(12), "Name".ljust(15), "Course".ljust(15), "Fees".ljust(12), "City".ljust(15))
    for row in res:
        print(str(row[0]).ljust(12), str(row[1]).ljust(15), str(row[2]).ljust(15), str(row[3]).ljust(12), str(row[4]).ljust(15)) 

def update_fees(id,fees):
    q="update student_pdbc set fees=%s where sid=%s"
    cursor.execute(q,(fees,id))
    conn.commit()
    if cursor.rowcount>0:
        print("record updated succesfully")
    else:
        print("record not found")
def delete(sid):
    q="delete from student_pdbc where sid=%s"
    cursor.execute(q,(sid,))
    conn.commit()
    if cursor.rowcount>0:
        print("Record deleted succesfully")
    else:
        print("No record found")          
while True:
   print("""===== STUDENT MANAGEMENT SYSTEM =====
   1. Add Student
   2. Display All Students
   3. Search Student by Name
   4. Update Student Fees
   5. Delete Student
   6. Exit
   """)
   choice=int(input("Enter your choice:"))
   match choice:
    case 1:
        print("Enter details for  student")
        sid=int(input("enter student id:"))
        sname=input("Enter student name:")
        course=input("Enter course:")
        fees=float(input("enter fees:"))
        city=input("enter city:")
        data=(sid,sname,course,fees,city)
        addStudent(data)
    case 2 :
        Display()
    case 3 :
        name=input("Enter name:")
        search(name)   
    case 4 :
        id=int(input("enter studebnt id"))
        fees=float(input("enter new fees:"))
        update_fees(id,fees)  
    case 5 :
        sid=int(input("Enter student id :"))
        delete(sid)           
    case 6:
        print("thankyou for using student management system")
        break
cursor.close()
conn.close()