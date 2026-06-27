import matplotlib.pyplot as plt
import numpy as np

x=np.array([2021,2022,2023,2024,2025])     
y=np.array([15,18,24,29,13])   

plt.title("Ferrari's sold",fontsize=20,
                           family="Arial",
                           fontweight="bold",
                           color="black")

plt.xlabel("Year",fontsize=15,
                  family="Arial",
                  fontweight="bold",
                  color="green")

plt.ylabel("Units sold",fontsize=15,
                        family="Arial",
                        fontweight="bold",
                        color="orange")

plt.tick_params(axis="x",
                color="blue")
plt.tick_params(axis="y",
                color="red")
#or we can also do plt.tick_params(axis="both",colors="red")

plt.grid(axis="both",               #or we can give x or y
         linewidth=1,
         color="gray",
         linestyle="dashed")

plt.plot(x,y)
plt.xticks(x)                       #so that only x values are shown as x ticks
plt.show()