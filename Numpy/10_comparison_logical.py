import numpy as np

#//////////////////////Comparison operators///////////////////////
a=np.array([2,3,4])
b=np.array([4,9,2])
c=np.array([2,3,4])
d=np.array([2,3,5])
print(a==b)                             #compares each element
print(a==c)
print(c==d)

print(np.array_equal(a,b))              #compares arrays as whole
print(np.array_equal(a,c))

print(a>2)                              #returns True for all values greater than 2
a[a<=2]=0                               #replaces all elements less than equal to 2 to 0
print(a)

#///////////////////////Logical operators///////////////////////
a=np.array([True,True,False])
b=np.array([True,False,True])
print(np.logical_or(a,b))
print(np.logical_and(a,b))


