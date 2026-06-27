import numpy as np

arr=np.array([[10,20,30,40,50],
              [60,70,80,90,100]])
print(np.min(arr))
print(np.argmin(arr))               #position of min
print(np.max(arr))
print(np.argmax(arr))               #position of max
print(np.sum(arr))
print(np.mean(arr))
print(np.average(arr))
print(np.std(arr))
print(np.var(arr))
print(np.median(arr))

print(np.sum(arr,axis=0))           #column wise aggregation
print(np.sum(arr,axis=1))           #row wise aggregation