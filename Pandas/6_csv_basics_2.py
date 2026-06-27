import pandas as pd

stands=pd.read_csv("stands.csv")
pokemon=pd.read_csv("pokemon.csv")

#FILTERING
print("S category stands")
goat=stands[(stands["Power"]=="A") | (stands["Speed"]=="A")]
print(goat[["Stand_User","Stand_Name","Part"]])
print()

print("Tall pokemon")
tallpokemon=pokemon[pokemon["Height"]>=2]
print(tallpokemon[["Name","Type1","Type2"]])
print()

#AGGREGATE FUNCTIONS AND GROUPBY
print(pokemon.sum(numeric_only=True))
print()
print(pokemon.mean(numeric_only=True))
print()
print(pokemon.min(numeric_only=True))
print()
print(pokemon.max(numeric_only=True))
print()
print(pokemon.count(numeric_only=True))
print()

print("Number of types")
print(pokemon[["Type1","No"]].groupby("Type1").count())
print()

print("Tallest in each type")
print(pokemon[["Name","Type1","Height"]].groupby("Type1").max())

