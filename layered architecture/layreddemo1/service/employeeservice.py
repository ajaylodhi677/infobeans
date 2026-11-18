from dao.employeedao import EmployeeDao
class EmployeeService:
    def getemployee(self):
        print("service: processing employee request")

        dao=EmployeeDao()
        dao.get_employee()