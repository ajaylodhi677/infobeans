#smart loan risk categirizes
salary=int(input("Enter salary"))
credit=int(input("Enter credit score"))
exit =int(input("existing loan"))

if salary>=30000:
    if credit>=750:
       if exit==0:
          print("assign low risk")
       elif exit<=2:
          print("medium risk")
       else:
          print("high risk")
    elif salary>=50000:
       if credit>=650:
          print("medium risk")
       else:
          print("high risk")
else:
    print("Not eligible for loan")