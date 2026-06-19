d1,t1 = map(float,input(" Enter distance and time for trip 1").split())
d2,t2 = map(float,input(" Enter distance and time for trip 1").split())

totaldistance= d1+d2
totaltime = t1+t2

average = totaldistance/totaltime
print("average speed = ",average)
