import matplotlib.pyplot as plt
import numpy as np

#//////////////////////////////Vertical barchart////////////////////////////////
quantities=np.array([27,13,16,21,18,28,16])                     #y axis values
days=np.array(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])      #x axis values      (String arrays dont really benefit from NumPy like integer arrays)

label_details=dict(family="Arial",
                   fontweight="bold",
                   color="green")

plt.title("Chocolates consumed",fontsize=20,**label_details)
plt.xlabel("Days",fontsize=15,**label_details)
plt.ylabel("No. of chocolates",fontsize=15,**label_details)
plt.tick_params(axis="both",colors="red")

plt.bar(days,quantities,color="pink")
plt.show()

#//////////////////////////////Horizontal barchart////////////////////////////////
plt.title("Chocolates consumed",fontsize=20,**label_details)
plt.ylabel("Days",fontsize=15,**label_details)
plt.xlabel("No. of chocolates",fontsize=15,**label_details)
plt.tick_params(axis="both",colors="red")

plt.barh(days,quantities,color="pink")          
plt.show()