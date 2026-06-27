import numpy as np

#/////////////////Scalar arithmetic/////////////////
a1=np.array([1,2,3])
print(a1+2)
print(a1-1)
print(a1*2)
print(a1/2)
print(a1//2)
print(a1**2)

#//////////////////Array-array arithmetic////////////////
a1=np.array([1,2,3])
a2=np.array([3,6,9])
print(a2+a1)
print(a2-a1)
print(a2*a1)        #not matrix multiplication
print(a2**a1)
print(a2/a1)
print(a2//a1)

#///////////////////Dot product///////////////////
a1=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
a2=np.array([[1,0,2],
             [3,5,7],
             [2,4,6]])
res=np.dot(a1,a2)
print(res)

#//////////////////Matrices////////////////////
# 2d arrays and matrices are not the same
a1=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
a2=np.array([[1,0,2],
             [3,5,7],
             [2,4,6]])
a=np.asmatrix(a1)
b=np.asmatrix(a2)
print(a1*a2)
print(a*b)      #dot product