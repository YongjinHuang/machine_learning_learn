import numpy as np


def print_solutions(x1, x2, y, k=10):
    for alpha in np.random.rand(k):
        w2 = alpha
        w1 = (y - w2 * x2) / x1
        print("w1: %f, w2: %f" % (w1, w2))


print_solutions(3, 4, 8)
