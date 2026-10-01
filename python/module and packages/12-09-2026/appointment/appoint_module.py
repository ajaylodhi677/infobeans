def book_appoinment(appoinment):
    d={}
    id=int(input("Enter appointment id:"))
    pid=int(input("Enter patinent id:"))
    did=int(input("Enter doctor id:"))
    date=input("Enter date:")
    time=input("Enter appointment time:")
    d["appointment id"]=id
    d["patient id"]=pid
    d["Doctor id"]=did
    d["Appointment date"]=date
    d["appointment Time"]=time
    appoinment.append(d)
    return appoinment

def show_appointments(appoinment):
      for x in appoinment:
        for k,v in x.items():
            print(k.ljust(15),"=",v)  
        print()