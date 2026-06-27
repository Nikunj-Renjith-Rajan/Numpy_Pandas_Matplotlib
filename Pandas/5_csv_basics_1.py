import pandas as pd

stands=pd.read_csv("stands.csv")       
print(stands)
print()

pokemon=pd.read_csv("pokemon.csv").to_string()         #doesn't show all rows since too much data, so use .to_string()
print(pokemon)
print()

pokemon=pd.read_csv("pokemon.csv",index_col="No").to_string()         #index_col is used to set any column as the index
print(pokemon)
print()

#SELECTION BY COLUMN
print(stands["Stand_User"])
print()
print(stands[["Stand_User","Stand_Name"]])

#SELECTION BY ROWS  ->  .loc[]
stands=pd.read_csv("stands.csv",index_col="Stand_User")         #For our convenience, let us change the index_col       
print(stands)
print()

print(stands.loc["Diego Brando"])
print()

print(stands.loc["Diego Brando",["Stand_Name","Part"]])         #Choosing desired columns
print() 

print(stands.loc["Diego Brando":"Funny Valentine",["Stand_Name","Part"]])           #Selecting from a range of rows

#SELECTION BY ROWS  ->  .iloc[]
print(stands.iloc[0:11,0:2])         #Choosing desired columns
print()

print(stands.iloc[0:11:3,0:2])         #Similar to python and numpy [low,high,step]
print()

#READING FROM USER
stands=pd.read_csv("stands.csv",index_col="Stand_User")
name=input("Read Stand-User name:")
try:
    print(stands.loc[name])
except KeyError:
    print(f"{name} not found in db")
