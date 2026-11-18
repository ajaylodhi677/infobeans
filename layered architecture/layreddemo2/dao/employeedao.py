from database.connection import Database
class EmployeeDao:
    def saveemployee(self,employee):
        print("Dao :saving employee data")
        print("Id :",employee.id)
        print("name :",employee.name)
        print("salary :",employee.salary)
        db=Database()
        db.connect()

