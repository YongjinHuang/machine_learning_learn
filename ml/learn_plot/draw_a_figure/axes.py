import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 256)
y = np.exp(x)
axe = plt.subplot()
axe.plot(x, y)
plt.show()
