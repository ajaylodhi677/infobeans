from service.employeeservice import EmployeeService
from model.Employee import Employee
print("welcome ")
employee=Employee(101,'ajay',50000)
service=EmployeeService()
service.addemployee(employee)
 