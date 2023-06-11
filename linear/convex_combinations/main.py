import numpy as np
import matplotlib.pyplot as plt

I = plt.imread('../../data/imgs/aged.jpeg')
J = plt.imread('../../data/imgs/young.jpeg')
n = 20
fig, ax = plt.subplots(1, n, figsize=(10, 10))

for i, alpha in zip(np.arange(n), np.linspace(0, 1, n)):
    im = (1-alpha)*I + alpha*J
    ax[i].imshow(im.astype(np.uint8), cmap='bone')
    ax[i].axis('off')
    ax[i].set_title(str(np.round(alpha, 2)))

plt.show()
