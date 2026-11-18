from service.employeeservice import EmployeeService
from model.Employee import Employee
print("welcome to our software")
service=EmployeeService()
while True:
    print("""\n1.Add Employee
2.Disply All employee
3.search by Id
4.update by id
5.delete by id
6.Exit
    """)
    choice=int(input("Enter your choice:"))
    match choice:
        case 1 :
            id=int(input("Enter employee id:"))
            name=input("Enter employee name:")
            salary=float(input("Enter salary:"))
            employee=Employee(id,name,salary)
            service.addemployee(employee)
        case 2 :
            service.displayAllemployee()
        case 3 :
            id=int(input("Enter employee id:"))
            service.searchemployeebyid(id)    
        case 4 :
            id=int(input("Enter employee id:"))
            salary=float(input("Enter new salary"))
            service.updateempsalbyid(id,salary)
        case 5 :
            id=int(input("Enter employee id:"))
            service.delemployeebyid(id)        
        case 6:
            print("Thanks for using program")
            service.closeConnection()
            break
        case _ :
            print("invaild choice")  
            
