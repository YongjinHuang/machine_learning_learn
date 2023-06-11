import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
import seaborn as sns

x1, x2, x3, y = np.loadtxt('pizza_3_vars.txt', skiprows=1, unpack=True)
# These weights came out of the training phase
w = np.array([-3.98230894, 0.37333539, 1.69202346])

sns.set(rc={'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('Temperature', labelpad=15, fontsize=14)
ax.set_ylabel('Reservations', labelpad=15, fontsize=14)
ax.set_zlabel('Pizzas', labelpad=5, fontsize=14)
ax.scatter3D(x1, x2, y, color='b')

MARGIN = 10
edges_x = [np.min(x1) - MARGIN, np.max(x1) + MARGIN]
edges_y = [np.min(x2) - MARGIN, np.max(x2) + MARGIN]
xs, ys = np.meshgrid(edges_x, edges_y)
zs = np.array([w[0] + x * w[1] + y * w[2] for x, y in
               zip(np.ravel(xs), np.ravel(ys))])
ax.plot_surface(xs, ys, zs.reshape((2, 2)), alpha=0.2)

plt.show()
