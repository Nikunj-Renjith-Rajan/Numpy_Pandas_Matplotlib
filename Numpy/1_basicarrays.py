import numpy as np

arr1=np.array([1,2,3,4])            #Numpy array
print(arr1)
print(type(arr1))

arr2=[1,2,3,4]                      #Normal python list
print(arr2)
print(type(arr2))       

print(arr1*2)                       #[2 4 6 8]  (Similarly all other scalar operations can be done)
print(arr2*2)                       #[1,2,3,4,1,2,3,4]

#//////////////////////Converting celsius to farenheit/////////////////////////
C=np.array([20.8,27.8,30.2,37.4,34.9])
print(C*9/5+32)

#//////////////////////Memory usage/////////////////////////
from sys import getsizeof as size
a=np.array([1,2,3])
b=np.array([])
print(size(a))
print(size(b))


