"""
Assignment 8: Car Mileage Calculator

 A car owner wants to calculate the mileage and fuel cost of a journey.

Create a class Car with the following attributes:

Car brand

Car model

Distance travelled in km

Fuel consumed in litres

Petrol price per litre

Create the following methods:

calculate_mileage() – Calculate kilometres per litre.

calculate_fuel_cost() – Calculate total fuel cost.

display_trip_details() – Display car and journey details.

Formulas:

Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price

Sample data:

Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105
"""
class Car:
    def __init__(self):
       self.cbrand=input("Enter car brand:")
       self.cmodel=input("Enter car model:")
       self.distance=int(input("Enter distance travelled in km:"))
       self.fuel=int(input("Enter Fuel Consumed:"))
       self.petrol_price=int(input("Enter price of petrol:"))
    def mileage(self):
       self.mileage=self.distance/self.fuel
    def calculate_fuel_cost(self):
        self.cost=self.fuel*self.petrol_price 
    def display_trip_details(self):
        print("Trip details are showing below")
        print("Car brand:",self.cbrand)
        print("Car model:",self.cmodel)
        print("Total distance:",self.distance)
        print("Fuel consumed:",self.fuel)
        print("Mileage :",self.mileage) 
        print("Total cost:",self.cost)     
c1=Car()
c1.calculate_fuel_cost()
c1.mileage()
c1.display_trip_details()        