"""
 2. Employee Salary Report

A company stores employee salary information in employees.txt.

Each record contains:

EmployeeID,EmployeeName,Department,Salary
Task

Write a Python program to:

Accept employee details.
Store them in the file.
Read the file.
Display employees whose salary is greater than ₹50,000.
Calculate the average salary.
Sample Input
Enter number of employees: 4

101,Ajay,IT,65000
102,Ravi,HR,45000
103,Priya,IT,72000
104,Amit,Sales,48000
Expected Output
Employees with Salary > 50000
--------------------------------
101  Ajay   IT       65000
103  Priya  IT       72000

Average Salary: 57500.00
"""
try:
    with open("Employee.txt","w+") as e:
        n=int(input("Enter number of employee:"))
        for i in range(n):
            print(f"Enter details of {i+1} Employee:")
            id=input("Enter Employee id:")
            name=input("Enter Employee name:")
            department=input("Enter department:")
            salary=input("Enter salary:")
            e.write(id+" "+name+" "+department+" "+str(salary)+"\n")
        e.seek(0)    
        total=0    
        for line in e:
            parts=line.split()
            total+=int(parts[3])
            if int(parts[3])>50000:
                print(line,end="")
        print("Average salary :",total/n)

except FileNotFoundError:
    print("invalid file name")            