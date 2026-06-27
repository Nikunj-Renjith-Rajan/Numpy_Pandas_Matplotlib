#////////////////////////ones,zeros,empty/////////////////////////
# ones method can be used to create a numpy array containing 1s 
# similarly zeros with 0s
# and empty with arbitrary values
import numpy as np

print(np.ones((3,4)))               #float by default
print(np.ones((3,4),dtype=int))

print(np.zeros((4,3)))

arr=np.array([0,1,2,3,4,5])
print(np.ones_like(arr))
print(np.zeros_like(arr))
print(np.trim_zeros(arr))           #removes zeros from the array

print(np.empty((2,4)))              #arbitrary values are given in the array