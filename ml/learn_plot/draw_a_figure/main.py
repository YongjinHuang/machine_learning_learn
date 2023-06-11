import numpy as np
import matplotlib.pyplot as plt

# step1 : create a dataset
points = np.linspace(-5, 5, 256)
y1 = np.power(points, 3) + 2.0
y2 = np.sin(points) - 1.0
# step2 : create a canvas
fig, axe = plt.subplots()
# step3 : add data to axes
axe.plot(points, y1)
axe.plot(points, y2)
# step4 : show the figure
plt.show()
