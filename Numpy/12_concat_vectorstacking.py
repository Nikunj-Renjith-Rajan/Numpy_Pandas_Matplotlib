#////////////////////////Concatenating/////////////////////////
import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([6,7,8])
a=np.array([[1,2],
            [3,4]])
b=np.array([[0,0],
            [0,0]])
print(np.concatenate((arr1,arr2)))
print(np.concatenate((a,b)))
print(np.concatenate((a,b),axis=1))

#//////////////////////Vector stacking////////////////////////////
print(np.column_stack((a,b)))
print(np.vstack((a,b)))             #row_stack

#///////////////////Tile:Repeating patterns//////////////////////
x=np.array([[1,2],[3,4]])
y=np.array([3.4])
print(np.tile(x,(2,3)))
print(np.tile(y,5))