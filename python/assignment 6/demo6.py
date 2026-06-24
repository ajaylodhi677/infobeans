salary = int(input("Enter your salary"))
exp = int(input("Enter your experience"))


if exp>=10:
    print("bonus amount :",salary*0.20)
elif exp>=5:
    print("bonus amount :",salary*0.10)
elif exp>=2:
    print("bonus amount:",salary*0.05)
else:
    print("no bonus")