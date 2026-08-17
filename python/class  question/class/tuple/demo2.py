from collections import namedtuple
Student=namedtuple("Students",["rollno","name","marks"])
n=int(input("Enter number of students :"))
students=[]
for i in range(n):
    print("Enter details :")
    r=int(input("Enter rollno :"))
    name =input("Enter name :")
    m=float(input("Enter marks"))
    s=Student(r,name,m)
    students.append(s)
print(students)
for x in students:
     print(x.name,"and",x.marks)