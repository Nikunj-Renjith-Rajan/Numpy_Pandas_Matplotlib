# Histogram is a visual representation of the distribution ofquantitative data. 
# They group values into bins (intervals) and counts how many fall in each range.

import numpy as np
import matplotlib.pyplot as plt

scores=np.random.normal(loc=70,scale=20,size=100)   #loc is the median value, scale is the standard deviation and size denotes the number of elements
scores=np.clip(scores,0,100)

plt.title("Exam scores",fontsize=20,
                        family="Arial",
                        fontweight="bold")
plt.xlabel("Scores",fontsize=20,
                        family="Arial",
                        fontweight="bold")
plt.ylabel("No of students",fontsize=20,
                        family="Arial",
                        fontweight="bold")

plt.hist(scores,bins=8,
                color="lightgreen",
                edgecolor="black")

plt.show()