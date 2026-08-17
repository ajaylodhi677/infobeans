#petrol cost calculation 
d ,m, p = map(int, input("Enter distance in km milage in km/land petrol price  respectively").split())

petrol = d/m
cost = petrol*p

print("petrol used " ,petrol,"liters")
print("total cost : ",cost)