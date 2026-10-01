def generate_bill(bill,patient):
    id=int(input("Enter patient id"))
    for x in patient:
        if id==x["patient id"]:
            charge=int(input("Enter consultation charges:"))
            mcost=int(input("Enter medition cost:"))
            tcost=int(input("Enter test charges:"))
            bilamount=charge+mcost+tcost
            print("\n============bill=======================")
            print("Patient id:",x["patient id"])
            print("patient name:",x["name"])
            print("Disease:",x["disease"])
            print()
            print("consultation fees:",charge)
            print("Medition cost:",mcost)
            print("Test charges:",tcost)
            print("=="*15)
            print("Total bilamount:",bilamount)
            break    
    else:
        print("Patient not registered")
