cp , sp = map(float,input(" Enter cost price and selling price").split())

pl = sp-cp
plper = pl/cp*100

print("profit/loss",pl)
print("profit/loss%",plper)