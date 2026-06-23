exp = int(input("Enter experience in years"))
rating = int(input("Enter ratings"))
salary = int(input("Enter salary"))

if exp>=5:
    if rating>=4:
       if salary<50000:
         print("bonus :",salary*0.20)
       else:
         print("bonus :",salary*0.10)
    else:
       print("bonus :",salary*0.05)
else:
    print("not elegible for bonjus")