#/////////////////Slicing/////////////////
#[start:end:step] for both row and column
#[start,end)
import numpy as np

arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [2,4,6,8],
              [1,3,5,7]])

print("row slicing")
print(arr[0:2])             #2 is excluded
print(arr[::-1])            #reversing
print(arr[::2])            #every 2nd row is printed 
print()

print("column slicing")
print(arr[:,0:2])             #2 is excluded
print(arr[:,::-1])            #reversing
print(arr[:,::2]) 
print()

print("row and column slicing")
print(arr[:2,:2])                #printing quadrant
print(arr[::-1,::-1])            #reversing
print(arr[2:,:1:-1])
print()

print("Similarly for 3d arras also")
x2=np.array([[[1,2,3],[4,5,6]],
             [[1,3,5],[2,4,6]]])
print(x2[::-1,::-1,::-1])