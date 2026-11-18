import numpy as np
a=np.array([1,2,3,4,5,6])
print(type(a))
b=np.zeros(5)
print(b)
c=np.ones(5,dtype=int)
print(c)
print(np.full(5,"kp"))

d=np.arange(1,5)
print(d)

e=np.arange(1,10,2)
print(e)

#f=np.linspace(0,10)
#print(f)

g=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(g)            

h=np.eye(3,dtype=int)
print(h)

i=np.zeros((2,3),dtype=int)
print(i)