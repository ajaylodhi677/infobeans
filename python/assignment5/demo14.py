age =int(input("Eter age"))
weight=int(input("enter weight"))
goal = input(" enter goal weight loss/muscles gain")

if age>=18:
    if weight>=80:
       if goal=='weight loss':
          print(" plan = cardio plan")
       else:
          print(" plan = strength plan")
    else:
       print("plan = general fitnessplan")
else:
    print(" not allowed for zym")
