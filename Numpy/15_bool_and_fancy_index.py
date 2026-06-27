import numpy as np

#//////////////////////BOOLEAN INDEXING///////////////////////
# returns True for the ones that satisfy condition and False elsewhere
print("BOOLEAN INDEXING")
arr=np.array([1,2,3,4,5,6,7])
print(arr>3)
print(arr%2==0)
print()

#/////////////////////FANCY INDEXING////////////////////////
# indexing an array with a boolean mask
print("FANCY INDEXING")
a=np.array([72,48,131,129,92,67,33])
b=np.array([4,7,11,19,13,2,26])
c=a[b%2==0]
d=a[(b>10) & (b<20)]
e=b[a>70]
print(c)
print(d)
print(e)