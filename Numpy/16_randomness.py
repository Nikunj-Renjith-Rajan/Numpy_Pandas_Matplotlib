import numpy as np

#///////////////////RANDOM INTEGER///////////////////
rng=np.random.default_rng()
print(rng.integers(low=1,high=10))               #.integers(low,high,size) also equivalent to .integers(1,10)
print(rng.integers(1,10,size=3))
print(rng.integers(1,10,size=(2,3)))

rng=np.random.default_rng(seed=1)               #seed is set if we want to get the same output after each compilation
print(rng.integers(1,10,size=3))

#//////////////////RANDOM FLOAT//////////////////////
print(np.random.uniform())                      #By default a number between 0 and 1 gets printed
print(np.random.uniform(low=-1,high=1))
print(np.random.uniform(low=-1,high=1,size=3))

rng=np.random.seed(seed=1)                      #Like before, setting a seed
print(np.random.uniform(low=1,high=5))

#///////////////////Shuffling an array////////////////////////
arr=np.array([1,2,3,4,5])
rng=np.random.default_rng()                     #seed can be introduced just as seen before
print("Before shuffling:",arr)
rng.shuffle(arr)
print("After shuffling:",arr)

#/////////////////////Random choice////////////////////////
rng=np.random.default_rng()
epics=np.array(['Rummenigge','Romario','Gullit','Maldini','Etoo','Beckham','Nedved','Nesta','Cech'])
surprise=rng.choice(epics)
print(surprise)
surprise=rng.choice(epics,size=(2,2))
print(surprise)
