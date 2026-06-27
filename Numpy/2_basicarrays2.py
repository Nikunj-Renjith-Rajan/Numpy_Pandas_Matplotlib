#creating arrays with equally spaced elements
import numpy as np

#////////////////arange(start,stop,step,dtype=None)/////////////////
x=np.arange(1,10)                           #10 is not inclusive
y=np.arange(10.4)                           #arbitrarily starts from zero
z=np.arange(0.5,10.4,0.8)
print(x)
print(y)
print(z)

#///////////////linspace(start,stop,num=50,endpoint=True,retstep=False)////////////////
a=np.linspace(1,10,10,endpoint=False)
print(a)