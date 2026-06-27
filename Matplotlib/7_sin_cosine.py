import numpy as np
import matplotlib.pyplot as plt

pi=np.pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 50, endpoint=True)
sinfn=np.sin(x)
cosfn=np.cos(x)

plt.plot(x,sinfn,alpha=0.5)
plt.plot(x,cosfn,color="red",
                 linestyle="dashed")
plt.show()