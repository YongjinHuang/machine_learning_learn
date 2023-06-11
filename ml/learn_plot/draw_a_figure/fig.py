import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 256)
y = 2 * x + 1

fig = plt.figure(dpi=300)
plot = fig.add_subplot(111)
plot.plot(x, y)
fig.show()
