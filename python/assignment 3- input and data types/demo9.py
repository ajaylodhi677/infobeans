# fuel cost calculator

d , m , p = map(float,input(" enter distance in km and milage in km/l and price if fuel ").split())

# calulate cost
avg = d/m
cost = avg*p

print(" cost :", cost)