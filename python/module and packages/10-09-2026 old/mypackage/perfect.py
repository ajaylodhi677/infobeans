def Perfect(num):
    sum=0
    for i in range(num//2+1):
        if num%i==0:
            sum+=i
    if num==sum:
        return "Perfect number"
    else:
        return "Not perfct number"            