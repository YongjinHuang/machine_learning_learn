import numpy as np


def predict(x, w):
    return np.matmul(x, w)


def loss(x, y, w):
    return np.average((predict(x, w) - y) ** 2)


def gradient(x, y, w):
    return 2 * np.matmul(x.T, predict(x, w) - y) / x.shape[0]


def train(x, y, iteration, lr):
    w = np.zeros((x.shape[1], 1))
    for i in range(iteration):
        print("Iteration %4d => Loss: %.10f" % (i, loss(x, y, w)))
        dw = gradient(x, y, w) * lr
        w -= dw
    return w


if __name__ == '__main__':
    pollution, healthcare, water, life = np.loadtxt('life-expectancy-without-country-names.txt', skiprows=1,
                                                    unpack=True)
    xinput = np.column_stack((np.ones(pollution.size), pollution, healthcare, water))
    yinput = life.reshape(-1, 1)
    print(xinput.shape, yinput.shape)
    weight = train(xinput, yinput, iteration=100, lr=0.0001)
    print("hello", weight)
    for i in range(10):
        print("X[%d] -> %.4f (label: %d)" % (i, predict(xinput[i], weight), yinput[i]))
