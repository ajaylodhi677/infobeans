# comound intersrt calculator
p,r,t = map(float,input(" Enter principal , rate of interst and time respectively").split())

amount = int(p*(1+r/100)**t)
ci = amount -p

print("amount ",amount)
print("Compound interest",ci)