import numpy as np


# computing the predictions
def predict(x, w):
    return np.matmul(x, w)


# calculating the loss
def loss(x, y, w):
    return np.average((predict(x, w) - y) ** 2)


# evaluating the gradient
def gradient(x, y, w):
    return 2 * np.matmul(x.T, (predict(x, w) - y)) / x.shape[0]


def train(x, y, iterations, lr):
    w = np.zeros((x.shape[1], 1))
    for i in range(iterations):
        print("Iteration %4d => Loss: %.10f" % (i, loss(x, y, w)))
        dw = gradient(x, y, w) * lr
        w -= dw
    return w


if __name__ == '__main__':
    x1, x2, x3, y = np.loadtxt('pizza_3_vars.txt', skiprows=1, unpack=True)
    x = np.column_stack((np.ones(x1.size), x1, x2, x3))
    y = y.reshape(-1, 1)
    w = train(x, y, iterations=100000, lr=0.001)
    print("\nWeights: %s" % w.T)
    for i in range(5):
        print("X[%d] -> %.4f (label: %d)" % (i, predict(x[i], w), y[i]))
