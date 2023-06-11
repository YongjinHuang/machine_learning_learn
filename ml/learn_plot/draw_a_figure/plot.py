import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 256)
y = np.sin(x)
plt.plot(x, y)
plt.show()
