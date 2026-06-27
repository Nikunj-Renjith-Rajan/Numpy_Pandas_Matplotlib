#Series is a 1D labelled column
import pandas as pd

#Creating a series using an array
data=[100,102,104]
series=pd.Series(data)
print(series)
print(series.index)             #displays range of indices
print(series.values)            #displays values only
print()

#Creating a series using a dictionary
data={'Mango':150,'Orange':40,'Apple':150}
series=pd.Series(data)
print(series)
print(series.index)             #displays range of indices
print(series.values)            #displays values only
print()

#Giving index
data=[100,102,104]
series=pd.Series(data, index=['e1','e2','e3'])
print(series)
print(series.index)             #here it displays the indices
print()

#Accessing each value   ->  .loc[] and .iloc[]
print(series.loc['e2'])          #using label
print(series.iloc[1])           #using index position

series.iloc[1]=202
print(series)
print()


#Boolean filtering
print(series[series>150])
print('e3' in series)
print()


#Addition of 2 series, actually it is a union
data1=[31,34,45]
data2=[20,18,19]
data3=[12,80,37]
series1=pd.Series(data1, index=['e1','e2','e3'])
series2=pd.Series(data2, index=['e1','e2','e3'])
series3=pd.Series(data3, index=['e1','e0','e3'])
print(series1+series2)
print()
print(series1+series3)
