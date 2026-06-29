#VISUALIZING CUMULATIVE SCORE FOR STANDS 
import pandas as pd
import matplotlib.pyplot as plt

stands=pd.read_csv("stands.csv")
stats={'?':10,'X':7,'A':5,'B':4,'C':3,'D':2,'E':1}
stat_columns=['Power','Speed','Range','Stamina','Precision','Development']
numeric_stats_col=[]

for col in stat_columns:
    stands[col]=stands[col].map(stats).fillna(10)

stands['cumulative_stats'] = stands[stat_columns].sum(axis=1)

colourcode={"Part 3: Stardust Crusaders":"yellow",
            "Part 4: Diamond is Unbreakable":"pink",
            "Part 5: Golden Wind":"blue",
            "Part 6: Stone Ocean":"green",
            "Part 7: Steel Ball Run":"orange",
            "Part 8: JoJolion":"cyan"}
stands["Colour"]=stands["Part"].map(colourcode)
stands=stands.sort_values(by='cumulative_stats',ascending=False)

print(stands)

plt.figure(figsize=(8,6))
plt.bar(stands['Stand_Name'],stands['cumulative_stats'],color=stands['Colour'],edgecolor='black',alpha=0.8)
plt.xlabel("Stand Name")
plt.ylabel("Cumulative total score")
plt.xticks(rotation=90)
plt.title("Total Cumulative stats")
plt.grid(axis='y',linestyle='--',alpha=0.5)

plt.show()
