import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Reading the two images
im1 = plt.imread('../../data/imgs/aged.jpeg')
im2 = plt.imread('../../data/imgs/young.jpeg')

# Selecting number of frames (intermediate combinations) and interval between frames
NFRAMES = 100  # number of frames
FINTERV = 80  # interval between frames (in milliseconds)

# Generating an array of alphas, containing equally distributed values between 0 and 1 for each frame.
alphas = np.linspace(0, 1, NFRAMES)

# Creating fig holder with specific styling
rc('animation', html='html5')
fig, ax = plt.subplots()


# Function to generate a convex combination for each frame and returning the plot
def animation(frame):
    plt.cla()  # clear all axes
    img = alphas[frame] * im1 + (1 - alphas[frame]) * im2
    f = ax.imshow(img.astype(np.uint8))
    plt.close()
    return f


# Creating animations using FuncAnimation from matplotlib.
a = anim.FuncAnimation(fig, animation, frames=NFRAMES, interval=FINTERV)
a.save('hellow.gif', writer='pillow', fps=30)
