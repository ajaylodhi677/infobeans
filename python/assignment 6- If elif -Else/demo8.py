temperature = int(input("Enter temperature"))

if temperature<0:
    print(" weather condition :Freezing")
elif temperature>0 and temperature<=20:
    print("wearther condition :Cold")
elif temperature>20 and temperature<=35:
    print("wearther condition :Warm")
else:
    print("wearther condition :HOt")