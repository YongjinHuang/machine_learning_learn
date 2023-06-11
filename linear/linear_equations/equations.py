import matplotlib.pyplot as plt
import numpy as np

w2line1 = np.linspace(-5, 5, 10)
w2line2 = np.linspace(-5, 5, 10)
w1line1 = (9 + 4 * w2line1**2) / 2
w1line2 = (3 - 7 * w2line2**2) / 3
plt.plot(w2line1, w1line1, '-r')
plt.plot(w2line2, w1line2, '-b')
plt.title('R: l1, B: l2, G: Solution')
plt.plot(-21 / 26, (9 + 4 * (-21 / 26)) / 2, 'gs')
plt.show()
