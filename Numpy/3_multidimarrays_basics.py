import numpy as np

#//////////////////ndim//////////////////////
# returns the dimension of the array

#//////////////////shape/////////////////////
# returns the shape which is a tuple of integers (number of elements per axis)
# for a 2d array, it returns the number of rows (x) and number of columns respectively
# for a 3d array, it returns the number of rows, number of columns, and number of elements within a subarray

print("2d array")
x1=np.array([[1,2,3],
             [4,5,6]])
print(x1)
print(x1.ndim)
print(x1.shape)
print()

print("3d array")
x2=np.array([[[1,2,3],[4,5,6]],
             [[1,3,5],[2,4,6]]])
print(x2)
print(x2.ndim)
print(x2.shape)
print()

#Using shape method, we can also change the shape of arrays
print("Reshaping")
x1=np.array([[1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12],
             [13,14,15],
             [16,17,18]])
print(x1)                   
x1.shape=(3,6)              #initially shape was (6,3)
print(x1)


