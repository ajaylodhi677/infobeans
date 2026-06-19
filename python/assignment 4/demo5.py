sallary,days= map(int, input("enter your total salary and days of working").split())
hour= int(input("working hour per day"))

hour =hour*days
dwg= sallary/days
hwg= sallary/hour

print("salary per day =",dwg,"\n salary per hour:",hwg)
