"""
ASSIGNMENT 1 – STUDENT MANAGEMENT SYSTEM

Q1. Create a database named school_db and use the database.

Q2. Create a table named student with:
- student_id – INT, PRIMARY KEY, AUTO_INCREMENT
- student_name – VARCHAR(50)
- age – INT
- course – VARCHAR(50)
- city – VARCHAR(50)
- marks – INT

Q3. Insert the following 10 student records:

student_name | age | course | city | marks
Rahul Sharma | 21 | Python | Indore | 85
Priya Verma | 22 | Java | Bhopal | 78
Amit Singh | 20 | Python | Indore | 92
Neha Patel | 23 | Java | Pune | 81
Rohit Mehta | 21 | Python | Mumbai | 88
Sneha Jain | 22 | Java | Indore | 76
Karan Gupta | 20 | Python | Delhi | 95
Pooja Mishra | 23 | Java | Bhopal | 84
Ankit Tiwari | 21 | Python | Pune | 79
Riya Kapoor | 22 | Java | Mumbai | 91

Q4. Display the structure of the student table using DESC.

Q5. Display all records from the student table.

"""
create database school_db;
use school_db;
create table student(student_id int primary key AUTO_INCREMENT,
student_name VARCHAR(20),
age int,
course VARCHAR(50),
city VARCHAR(50),
marks int);
desc student;
insert into student(student_name,age,course,city,marks) values('rahul sharma',21,'python','indore',85);
insert into student(student_name,age,course,city,marks) values('Priya verma',22,'java','bhopal',78),
('amit singh',20,'pyhton','indore',92),
('neha patel',23,'java','pune',81),
('rohit mehta',21,'python','mumbai',88),
('sneha jain',22,'java','indore',76),
('karan gupta',20,'python','delhi',95),
('pooja mishra',23,'java','Bhopal',84),
('ankint tiwari',21,'python','mubai',79),
('riya kappor',22,'java','maubai',91);
desc student;
select *from student;