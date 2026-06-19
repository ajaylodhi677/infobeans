#Cricket Run Rate
runs =int(input("Enter total runs"))
overs=float(input("Enter overs"))

balls = overs//1
#print("balls",balls)
rem = (overs*10)%10
balls = int(balls*6+rem)
rate = (runs/balls)*6
print(" total balls :" ,balls, "\nrun rate :",rate)