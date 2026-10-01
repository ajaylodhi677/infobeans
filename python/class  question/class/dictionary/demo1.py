words=['dog','cat','tiger','four']
g={}
for x in words:
    length=len(x)
    g[length]=g.get(x,[]) 
    g[length].append(x)
print(g)