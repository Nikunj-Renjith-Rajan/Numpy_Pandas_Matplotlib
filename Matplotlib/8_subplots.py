# Figure : a figure is the entire canvas in which the plots are displayed
# Ax : a single plot (subplot)

#KERALA ELECTIONS
import numpy as np
import matplotlib.pyplot as plt

party=["LDF","UDF","NDA","Others"]
votes1=np.array([35,102,3,0])
votes2=np.array([91,47,1,1])
colorcode=["red","skyblue","orange","purple"]

figure,axes=plt.subplots(2,2)

axes[0,0].set_title("ELECTION RESULTS 2026-bar")
axes[0,0].bar(party,votes1,color=colorcode)

axes[0,1].set_title("ELECTION RESULTS 2026-pie")
axes[0,1].pie(votes1,labels=party,autopct="%1.1f%%",colors=colorcode)

axes[1,0].set_title("ELECTION RESULTS 2016-bar")
axes[1,0].bar(party,votes2,color=colorcode)

axes[1,1].set_title("ELECTION RESULTS 2016-pie")
axes[1,1].pie(votes2,labels=party,autopct="%1.1f%%",colors=colorcode)

plt.show()


