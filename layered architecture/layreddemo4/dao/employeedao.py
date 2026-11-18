from database.connection import Database
from model.Employee import Employee
db=Database()
connection=db.connect()
cursor=connection.cursor()
class EmployeeDao:
    def saveemployee(self,employee):
        print("Dao: saving employee")
        query="insert into employee values (%s,%s,%s)"
        values=(employee.id,employee.name,employee.salary)
        cursor.execute(query,values)
        print("saved into datbase succesfully")

    def getallEmployees(self):
        cursor.execute("select * from employee")
        res=cursor.fetchall()
        Employees=[]
        for row in res:
            employee=Employee(row[0],row[1],row[2])
            Employees.append(employee)
        return Employees
    def getEmployeebyid(self,eid):
        query="select * from employee where id=%s"
        cursor.execute(query,(eid,))
        res=cursor.fetchone()
        
        if res is not None:
            employee=Employee(res[0],res[1],res[2])
            return employee
        return None    
    def updatebyid(self,id,salary):
            query="update employee set salary=%s where id=%s"
            cursor.execute(query,(salary,id))
            if cursor.rowcount>0:
                print("Record updated successfully")
            else:
                print("No recor found with id:",id)    
    def deleteempbyid(self,id):
        query="delete from employee where id=%s"
        cursor.execute(query,(id,))
        if cursor.rowcount>0:
            print("Record deleted succesfully")
        else:
            print("No record found with id",id)    
    def closeConnection(self):
        cursor.close()
        connection.close()
        print("Database connection closed")        

            

        


