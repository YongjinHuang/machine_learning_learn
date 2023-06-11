import numpy as np
import matplotlib.pyplot as plt

# A legend provides a description for an element in the figure

points = np.linspace(-5, 5, 256)
y1 = np.tanh(points) + 0.5
y2 = np.sin(points) - 0.2

fig, axe = plt.subplots(nrows=1, ncols=2, dpi=800)
axe[0].plot(points, y1, label='tanh')
axe[0].plot(points, y2, label='sin')
# Adding a legend without labels
axe[0].legend()

axe[1].plot(points, y1)
axe[1].plot(points, y2)
# Adding a legend with labels
axe[1].legend(['tanh', 'sin'], loc='upper right', shadow=True)

plt.show()
