def pow(b,e):
    if e==0:
      return 1
    return b*pow(b,e-1)
print(pow(2,4))