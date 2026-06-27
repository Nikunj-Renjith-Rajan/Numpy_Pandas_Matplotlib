# Datframe is a 2D labelled table
import pandas as pd

#CREATING A DATAFRAME
cities = {"CLUB": ["Arsenal", "Bayern", "Barcelona", "Inter", "PSG"],
          "POPULATION": [8615246, 3562166, 3165235, 2874038, 2273305],
          "COUNTRY": ["England", "Germany", "Spain", "Italy", "France"]}
labels=["Premier League","Bundesliga","LaLiga","Serie A","Ligue 1"]         #SIMILAR TO SERIES, WE CAN PROVIDE CUSTOM INDICES
df=pd.DataFrame(cities,index=labels)
print(df)
print()

#RENAMING COLUMNS
print("RENAMING COLUMNS")
df.rename(columns={"CLUB":"FC","POPULATION":"STRENGTH","COUNTRY":"REGION"},inplace=True)
print(df)
print()

#REARRANGING COLUMNS
print("REARRANGING COLUMNS")
df=pd.DataFrame(cities,index=labels,columns=["CLUB","COUNTRY","POPULATION"])
print(df)
print()

#.loc[] AND .iloc[] FUCNTIONS EXIST JUST LIKE IN SERIES, FOR DATA ACCESSING 
print(df.loc["LaLiga"])
print()

print(df.iloc[2])
print()

#INSTEAD OF ACCESSING EACH ROW, WE CAN ALSO ACCESS EACH INDIVIDUAL VALUE AND ALSO CHANGE IT
df.loc["LaLiga","CLUB"]="Barca"
print(df.loc["LaLiga","CLUB"])
print()


#ADDING A NEW COLUMN
df["MVP"]= ["Odegaard","Kane","Yamal","Lautaro","Kvaratskhelia"]
print("UPDATED DATAFRAME")
print(df)
print()

#ADDING NEW ROWS
new_row=pd.DataFrame([{"CLUB":"InterMiami","COUNTRY":"USA","POPULATION":89768412,"MVP":"Messi"},
                      {"CLUB":"Zlatan FC","COUNTRY":"Zlatanland","POPULATION":1,"MVP":"Zlatan"}],
                        index=["MLS","LionLiga"])
df=pd.concat([df,new_row])
print(df)