import matplotlib.pyplot as plt
import numpy as np

#Using python list
x=[1,2,3,4,5]           #x axis elements
y=[15,18,24,29,13]      #y axis elements
plt.plot(x,y)
plt.show()

#Using NumPy array
x=np.array([1,2,3,4,5])
y=np.array([15,18,24,29,13])
plt.plot(x,y)
plt.show()

#///////////////////////////LINE CUSTOMIZATIONS////////////////////////////////
# maker, markersize, markerfacecolor, markeredgecolor, linestyle, linewidth, color
x=np.array([1,2,3,4,5])
y1=np.array([15,18,24,29,13])
y2=np.array([32,28,14,19,21])
plt.plot(x,y1,marker=".",
              markersize=30,
              markerfacecolor="cyan",
              markeredgecolor="red",
              linestyle="dashdot",
              linewidth=3,
              color="blue")
plt.plot(x,y2,marker=".",
              markersize=30,
              markerfacecolor="yellow",
              markeredgecolor="red",
              linestyle="solid",
              linewidth=3,
              color="black")
plt.show()

# Instead of giving all the details again and again we could just use a dictionary function and just unpack it during plotting, 
# with changing only necessary details for identifying each line
x=np.array([1,2,3,4,5])
y1=np.array([15,18,24,29,13])
y2=np.array([32,28,14,19,21])
linedetails=dict(marker=".",
                 markersize=30,
                 markerfacecolor="cyan",
                 markeredgecolor="red",
                 linestyle="dashed",
                 linewidth=3)
plt.plot(x,y1,color="blue",**linedetails)
plt.plot(x,y2,color="black",**linedetails)
plt.show()
