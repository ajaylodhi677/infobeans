"""
ASSIGNMENT 2 – EMPLOYEE MANAGEMENT SYSTEM

Q1. Create a database named company_db and use the database.

Q2. Create a table named employee with:
- employee_id – INT, PRIMARY KEY, AUTO_INCREMENT
- employee_name – VARCHAR(50)
- age – INT
- department – VARCHAR(50)
- designation – VARCHAR(50)
- salary – INT

Q3. Insert the following 10 employee records:

employee_name | age | department | designation | salary
Rahul Sharma | 28 | IT | Developer | 55000
Priya Verma | 26 | HR | Executive | 42000
Amit Singh | 30 | IT | Team Lead | 75000
Neha Patel | 27 | Finance | Accountant | 48000
Rohit Mehta | 32 | IT | Manager | 90000
Sneha Jain | 25 | Marketing | Executive | 40000
Karan Gupta | 29 | IT | Developer | 60000
Pooja Mishra | 31 | HR | Manager | 80000
Ankit Tiwari | 28 | Finance | Analyst | 65000
Riya Kapoor | 27 | Marketing | Manager | 70000

Q4. Display the structure of the employee table using DESC.

Q5. Display all records from the employee table.
"""
create database company_db;

use company_db;

create table employee(employee_id int primary key auto_increment,
employee_name varchar(50),
age int,
department varchar(50),
designation varchar(50),
salary int);

desc employee;

insert into employee(employee_name,age,department,designation,salary)
values('rahul sharma',28,'it','Developer',55000);
insert into employee(employee_name,age,department,designation,salary)
values('priya verma',26,'hr','executive',42000),
('amit singh',30,'it','Team lead',75000),
('neha patel',27,'Finance','accountant',48000),
('rohit mehta',32,'it','manager',90000),
('sneha jain',25,'Marketing','executive',40000),
('karan gupta',29,'it','developer',60000),
('pooja mishra',31,'hr','manager',80000),
('ankit tiwari',28,'finance','analyst',65000),
('riya kapoor',27,'marketing','manager',70000);

desc employee;

select * from employee;