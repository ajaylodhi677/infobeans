unit = int(input("Enter units consumed"))

if unit>=100:
    if unit>=300:
       print("high usage")
    else:
       if unit>=200:
          print("moderate usage")
       else:
          print("Normal usages")
else:
    print("Low usages")