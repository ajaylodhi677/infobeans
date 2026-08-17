"""4. Airline Ticket Pricing Engine

An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000"""

type =input("Class :").lower()
dist = int(input(" Distance :"))
time =input("Bokking :").lower()

if type=='business':
    if dist>1000:
       print("Ticket price : 8000")
    else:
       print("Ticket price : 5000")
elif dist>1000:
    if time=='early':
       print("Ticket price : 4000")
    else:
       print("Ticket price : 5000")
else:
    print("Ticket price : 1000")

