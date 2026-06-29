#Visualizing total number of pokemon of each type in Kanto pokedex
import pandas as pd
import matplotlib.pyplot as plt

pokemon=pd.read_csv("pokemon.csv")

type_data=pokemon[['Type1','No']].groupby('Type1').count()

colourcode={'Bug':'lightgreen',
            'Dragon':'cyan',
            'Electric':'yellow',
            'Fairy':'lavender',
            'Fighting':'brown',
            'Fire':'red',
            'Ghost':'violet',
            'Grass':'green',
            'Ground':'beige',
            'Ice':'skyblue',
            'Normal':'lightgray',
            'Poison':'purple',
            'Psychic':'pink',
            'Rock':'gray',
            'Water':'blue'}
type_data['color']=type_data.index.map(colourcode)
type_data=type_data.sort_values(by='No',ascending=False)
print(type_data)

plt.bar(type_data.index,type_data['No'],color=type_data['color'],edgecolor='black')
plt.xticks(rotation=90)
plt.xlabel('Type')
plt.ylabel('Number')
plt.grid(axis='y',linestyle='--',alpha=0.5)
plt.title("Kanto dex types",fontweight='bold',
                            fontsize=25,
                            color='Green')

plt.show()