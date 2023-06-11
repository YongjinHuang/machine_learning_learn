import numpy as np
import matplotlib.pyplot as plt
# The tick is a mark on the axis to show the position of the data point
points = np.linspace(-5, 5, 256)
y1 = np.tanh(points) + 0.5
y2 = np.sin(points) - 0.2

fig, axe = plt.subplots(nrows=1, ncols=2, figsize=(12.8, 4.8), dpi=600)
axe[0].plot(points, y1)
axe[0].plot(points, y2)

axe[1].plot(points, y1)
axe[1].plot(points, y2)
axe[1].set_xticks(np.linspace(-5, 5, 6))
axe[1].tick_params(colors='b')
plt.show()
