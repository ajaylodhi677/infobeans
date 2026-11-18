from dao.employeedao import EmployeeDao
dao=EmployeeDao()
class EmployeeService:
    def addemployee(self,employee):
        print("service: processing employee request")
        if employee.id<=0:
            print("Id should positive")
            return
        if employee.name.strip()=="":
            print("Name can not be empty") 
            return   
        dao.saveemployee(employee)

    def displayAllemployee(self):
        Employees=dao.getallEmployees()
        if len(Employees)==0:
            print("No employee found")
            return
        for employee in Employees:
            print("Id :",employee.id)
            print("name :",employee.name)
            print("salary :",employee.salary)

    def searchemployeebyid(self,id):
        employee=dao.getEmployeebyid(id)
        if employee is None:
            print("No record found")
        else:
            print("Id :",employee.id)
            print("name :",employee.name)
            print("Salary :",employee.salary)  
    def updateempsalbyid(self,id,salary):
        dao.updatebyid(id,salary)
    def delemployeebyid(self,id):
        dao.deleteempbyid(id)              
    def closeConnection(self):
        dao.closeConnection()

                

