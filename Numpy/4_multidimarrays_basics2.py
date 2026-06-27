#///////////////multidimensional indexing is possible in numpy/////////////////////
# multi-dimensional indexing is faster than chain indexing
import numpy as np

x1=np.array([[[1,2,3],[4,5,6]],
             [[1,3,5],[2,4,6]]])
x2=np.array([[['a','b','c'],['d','e','f']],
             [['g','h','i'],['j','k','l']]])
print(x2)
print(x2[0][0][1])                   #Normal python methodology -> chain indexing
print(x2[0,0,1])                     #Multi-dimensional indexing

print(x2[0,0,1]+x2[0,0,0]+x2[1,0,0])
print(x1[0,0,2]+x1[1,0,2])
print()

#///////////////////reshape////////////////////////
# reshape method is used to construct a multi-dimensional array from a 1d array
# it can be used with arange and linspace
print("reshape")
print(np.arange(27).reshape(3,3,3))
print(np.arange(28).reshape(4,7))