import numpy as np
import matplotlib.pyplot as plt

# Spines are lines that connect the axis tick marks to one another
# Spines also note the data area boundaries
points = np.linspace(-5, 5, 256)
y1 = np.tanh(points) + 0.5
y2 = np.sin(points) - 0.2

fig, axe = plt.subplots(dpi=800)
axe.plot(points, y1)
axe.plot(points, y2)
axe.set_xticks(np.linspace(-5, 5, 9))
axe.spines['right'].set_visible(False)
axe.spines['top'].set_visible(False)
axe.spines['left'].set_position(('data', 0))
axe.spines['bottom'].set_position(('axes', 0.5))
plt.show()
