"""
kwargs
"""
def show(**kwargs):
   print("Id :",id)
   for k,v in kwargs.items():
        print(k.ljust(10),":",v)
show(101,name="ajay",age=19,adderess="chennai")