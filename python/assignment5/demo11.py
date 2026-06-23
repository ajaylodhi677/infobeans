# loan approval
salary=int(input("Enter salary"))
credit=int(input("Enter credit score"))
loan=int(input("how many existing loan"))

if salary>=30000:
    if credit>=750:
       print("laon apprived")
    else:
       if loan<2:
         print("conditionaly approverd")
       else:
         print("loan rejected")
else:
    print("loan rejected")