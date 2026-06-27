# Labels that don't have any value will display NaN (Not a Number). They are the missing data.
# Similarly, if in the dictionary a value is given as None for some label, that will also be displayed as NaN.
import pandas as pd

data={'Mango':150,'Orange':40,'Apple':150,'Strawberry':200,'Banana':30,'Pineapple':50}
arr=['Mango','Orange','Litchi','Apple','Kiwi']
s=pd.Series(data,index=arr)
print(s)                    #Here Litchi and Kiwi don't have any values (NaN)

#Checking which are null and which aren't
print(s.isnull()) 
print(s.notnull()) 

#Filtering out missing data
print(s.dropna()) 

#Filling in missing data
print(s.fillna(0))