from dao.employeedao import EmployeeDao
class EmployeeService:
    def addemployee(self,employee):
        print("service: processing employee request")

        dao=EmployeeDao()
        dao.saveemployee(employee)