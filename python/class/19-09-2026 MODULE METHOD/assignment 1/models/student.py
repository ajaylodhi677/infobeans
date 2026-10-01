class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
    def Display(students):
        for student in students:
             print(student.roll_no, student.name, student.marks)
    def highest(students):
        high=students[0]
        for Student in students:
            if high.marks<Student.marks:
                high=Student
        print(high.roll_no, high.name, high.marks)
        print(high)
    def average(students):
        total=0
        for Student in students:
             total+=Student.marks
        average=total/len(students)     
        print(f"{average:.1f}")        