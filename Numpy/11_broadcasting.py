#//////////////////////////////////BROADCASTING/////////////////////////////////////
# Broadcasting allows NumPy to perform operations on arrays with
# different shapes by virtually expanding dimensions so they match
# the larger array's shape
#
#CONDITION(For each pair of dimension):
#       ->dimensions are same
#               OR
#       ->one of the dimensions is 1
import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([[1],[2],[3],[4]])
arr3=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])
print(arr1.shape)               # 1x4
print(arr2.shape)               # 4X1
print(arr3.shape)               # 4X4
print(arr1*arr2)
print(arr1*arr3)

#Printing multiplication tables
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print()
print("MULTIPLICATION TABLE")
print(a*b)
