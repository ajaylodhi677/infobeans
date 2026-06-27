"""7. Ride Booking Surge Pricing System

A ride booking app calculates fare multiplier based on demand, time, and distance.

If demand is at least 80, then check time. If peak time, then check distance. If distance is at least 10, apply 2x fare; otherwise 1.5x. If not peak time, then check if demand is at least 90. If yes, 1.8x; otherwise 1.3x. If demand is less than 80, then check if demand is at least 50. If yes, then if peak time, apply 1.2x; otherwise normal fare. If demand is below 50, normal fare.

Input:
Demand = 85
Time = peak
Distance = 12

Output:
Fare Multiplier = 2x Fare"""


demand=int(input("Demand :"))
time =input("time :").lower()
dist=int(input("distance :"))

if demand>=80:  
    if time=='peak':
       if dist>=10:
          print("fare multiplier :2x Fare")
       else:
          print("fare multiplier :1.5x Fare")
    elif demand>=90:
       print("fare multiplier :1.8x Fare")
    else:
       print("fare multiplier :1.3x Fare")   
elif demand>=50:
    if time=='peak':
       print("fare multiplier :1.2x Fare")
    else:
       print("fare multiplier :normal Fare") 
else:
    print("fare multiplier :noraml")

