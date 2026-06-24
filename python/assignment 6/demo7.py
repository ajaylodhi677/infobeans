#banking withdrawl limit system
balance =int(input("Enter account balance"))

if balance<=1000:
    print("withdrawal not allowed")
elif balance>1000 and balance<=5000:
    print("maximum withdrawl 1000")
elif balance>5000:
    print("maximum withdrwal 5000")