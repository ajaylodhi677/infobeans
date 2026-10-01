def adddoc(doctor):
    d={}
    id=int(input("Enter doctor id:"))
    name=input("Enter doctor name:")
    sp=input("Enter speciality:")
    exp=input("Enter experience:")
    fees=int(input("Enter consultation fee:"))
    d["doc id"]=id
    d["name"]=name
    d["speciality"]=sp
    d["experience"]=exp
    d["fees"]=fees
    doctor.append(d)
    return doctor
#===========display patinet deatils===========    
def displaydoc(doctor):
    i=0
    for x in doctor:
        print(f"doctors {i+1} details")
        for k,v in x.items():
            print(k.ljust(10),"=",v)
        i+=1
        print()