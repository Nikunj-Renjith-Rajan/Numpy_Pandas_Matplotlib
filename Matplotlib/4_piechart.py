import matplotlib.pyplot as plt
import numpy as np

#Pie chart can be created using the function plt.pie()
categories=["Yes","Yes but in Yellow"]
values=np.array([190,10])
colorcode=["darkcyan","yellow"]

plt.title("Do you like JJBA?",fontsize=20,
                              family="Arial",
                              fontweight="bold",
                              color="purple")

plt.pie(values,                     
        labels=categories,
        autopct="%1.1f%%",
        colors=colorcode,
        explode=[0,0.2],
        shadow=True,
        startangle=45)
plt.show()