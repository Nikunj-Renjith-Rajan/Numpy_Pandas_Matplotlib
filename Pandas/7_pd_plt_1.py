import pandas as pd
import matplotlib.pyplot as plt

stands=pd.read_csv("stands.csv")
stats={'NA':10,'X':7,'A':5,'B':4,'C':3,'D':2,'E':1}
stat_columns=['Power','Speed','Range','Stamina','Precision','Development']
numeric_stats_col=[]

for col in stat_columns:
    # new_c_name=col+'_num'
    stands[col]=stands[col].map(stats)
    # numeric_stats_col.append(new_c_name)

# stands['cumulative_stats']=stands[numeric_stats_col].sum(axis=1)

print(stands)