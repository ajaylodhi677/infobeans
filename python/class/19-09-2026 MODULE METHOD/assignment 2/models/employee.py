class Employee:
    def __init__(self,employee_id,name,salary,department):
        self.employee_id=employee_id
        self.name=name
        self.salary=salary
        self.department=department

    def display(employees):
        for employee in employees:
            print(employee.employee_id,employee.name,employee.salary,employee.department)

    def salary_greater_than_40000(employees):
        for employee in employees:
            if employee.salary>40000:
                print(employee.employee_id,employee.name,employee.salary,employee.department)

    def it_department(employees):
        for employee in employees:
            if employee.department=="IT":
                print(employee.employee_id,employee.name,employee.salary,employee.department)

    def highest_salary(employees):
        high=employees[0]
        for employee in employees:
            if high.salary<employee.salary:
                high=employee
        print(high.employee_id,high.name,high.salary,high.department)

    def total_salary(employees):
        total=0
        for employee in employees:
            total+=employee.salary
        print(total)

    def average_salary(employees):
        total=0
        for employee in employees:
            total+=employee.salary
        average=total/len(employees)
        print(f"{average:.1f}")