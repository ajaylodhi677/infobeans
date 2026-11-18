from database.connection import Database
class EmployeeDao:
    def saveemployee(self,employee):
        print("Dao: saving employee")
        db=Database()
        connection=db.connect()
        cursor=connection.cursor()

        query="insert into employee values (%s,%s,%s)"
        values=(employee.id,employee.name,employee.salary)
        cursor.execute(query,values)
        connection.commit()
        cursor.close()
        connection.close()
        print("saved into datbase succesfully")


