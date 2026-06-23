age = int(input("Enter age "))
time=input("choose show time morning/evening").lower()
day = input("choose day weekday/weekend")

if age<18:
    if time=='morning':
       print(" ticket price =100")
    else:
       print(" ticket price =150")
else:
    if time=='evening':
       if day=='weekend':
          print(" ticket price :300")
       else:
          print(" ticket price :250")
    else:
       price("ticket price =200")