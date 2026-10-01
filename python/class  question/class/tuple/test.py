import time
#print(time.time())
print(time.ctime())
x=time.localtime()
print(x.tm_year)
print(x.tm_mon)
print(x.tm_mday)
print(x.tm_hour)