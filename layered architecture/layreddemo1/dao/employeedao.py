from database.connection import Database
class EmployeeDao:
    def get_employee(self):
        print("Dao getting employee data")
        db=Database()
        db.connect()

