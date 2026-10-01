#=================add patient details============
def addpatient(patient):
    d={}
    id=int(input("Enter patient id:"))
    name=input("Enter patient name:")
    age=int(input("Enter patient age:"))
    gender=input("Enter gender:")
    disease=input("Enter disease:")
    mob=int(input("Enter mobile number:"))
    d["patient id"]=id
    d["name"]=name
    d["age"]=age
    d["gender"]=gender
    d["disease"]=disease
    d["mobile number"]=mob
    patient.append(d)
    return patient 
#===========display patinet deatils===========    
def display(patient):
    i=0
    for x in patient:
        print(f"patient {i+1} details")
        for k,v in x.items():
            print(k.ljust(10),"=",v)
        i+=1
        print()
#def=========search patient ================
def search(id,patient):
    for x in patient:
        if id==x["patient id"]:
            for k,v in x.items():
                print(k.ljust(10),"=",v) 
            break      
    else:
        print("Patiend not found")    