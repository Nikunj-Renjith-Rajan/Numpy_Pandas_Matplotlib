#GROUP BY CLAUSE CAN BE USED AS USED IN MYSQL
import pandas as pd
import numpy as np

#///////////////////////////////////SERIES////////////////////////////////////
nvalues=20 #Say we have 20 values
rng=np.random.default_rng()
values=rng.integers(1,5,size=nvalues)
fruits=np.array(["Apple","Grapes","Mango","Orange"])
fruit_arr=rng.choice(fruits,size=(nvalues,))
fruitseries=pd.Series(values,index=fruit_arr)

print(fruitseries)
print()

print(fruitseries.groupby(fruitseries.index).sum())
print()

print(fruitseries.groupby(fruitseries.index).mean())
print()


#////////////////////////////////DATAFRAME///////////////////////////////////
beverages=pd.DataFrame({'Name': ['Robert', 'Melinda', 'Brenda','Samantha', 'Melinda', 'Robert','Melinda', 'Brenda', 'Samantha'],
                          'Coffee': [3, 0, 2, 2, 0, 2, 0, 1, 3],
                          'Tea': [0, 4, 2, 0, 3, 0, 3, 2, 0]})

print(beverages)
print()

print(beverages[['Coffee', 'Tea']].sum())       #Aggregation
print()

print(beverages.groupby(['Name']).sum())
print()
print(beverages.groupby(['Name']).mean())
