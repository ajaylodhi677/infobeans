p,r,t = map(int,input("Enter principal interest rate and time respectively ").split())

amount = p*(1+r/100)**t

print("Amount after interest :",amount) 