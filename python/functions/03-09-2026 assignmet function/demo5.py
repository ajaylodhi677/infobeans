
"""
QNO:
Employee Data Processing System

A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function and variable names and follow proper indentation
"""
def shigh(s):
   s=set(s)
   s=list(s)
   s=sorted(s)
   return s[-2]
def duplicate(s):
   ans=[]
   for x in s:
     if x not in ans:
        ans.append(x)
   return ans
def vowel(names):
   c=0
   for x in names:
      if x[0].lower() in "aeiou":
         c+=1
   return c
def longest(names):
   long=names[0]
   for x in names:
      if len(x)>len(long):
         long=x
   return long
emp=[]
while True:
  print("========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
  print("1. Find Second Highest Employee Age")
  print("2. Count Senior Employees")
  print("3. Remove Duplicate Ages") 
  print("4. Count Names Starting with a Vowel")
  print("5. Find Longest Employee Name")
  print("6. Exit")
  print("====================================================")
  choice =int(input("Enter your choice:"))
  match choice:
    case 1:
       emp=list(map(int,input("Enter employee age list:").split()))
       print("Second highest age :",shigh(emp))
    case 2 :
       emp=list(map(int,input("Enter employee age list:").split()))
       result=list(filter(lambda x:x>=50 ,emp))
       print("semiour employees :",len(result))
    case 3:
       emp=list(map(int,input("Enter employee age list:").split()))
       print("unique ages :",duplicate(emp))
    case 4:
       names=input("Enter employees name :").split()
       print("names start with vowel:",vowel(names))
    case 5:
       names=input("Enter employees name :").split()
       print("longest names :",longest(names))
    case 6:
       break
print("Thanks for using menu driven program ")