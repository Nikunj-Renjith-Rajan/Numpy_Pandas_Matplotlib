#/////////////////identity function/////////////////
# identity(n,dtype=float)
import numpy as np

print(np.identity(4))
print(np.identity(3,dtype=int))           #equivalent to np.identity(3,int)

#/////////////////////eye function//////////////////////
# eye(n,m=None,k=0,dtype=float)
# n is number of rows and m is number of columns
# k is the position from which the diagonal starts, set default to 0
print(np.eye(3))
print(np.eye(3,5))
print(np.eye(3,5,1))
print(np.eye(3,5,-1))


