import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea


def train(x, y, iterations, lr):
    w = b = 0
    for i in range(iterations):
        print("Iteration %4d => Loss: %.10f" % (i, loss(x, y, w, b)))
        w_gradient, b_gradient = gradient(x, y, w, b)
        w -= w_gradient * lr
        b -= b_gradient * lr
    return w, b


def predict(x, w, b):
    return x * w + b


def loss(x, y, w, b):
    return np.average((predict(x, w, b) - y) ** 2)


def gradient(x, y, w, b):
    return 2 * np.average(x * (predict(x, w, b) - y)), 2 * np.average(predict(x, w, b) - y)


def show_diagram(x, y, w, b):
    sea.set()
    plt.axis([0, 50, 0, 50])
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("Reservations", fontsize=14)
    plt.ylabel("Pizzas", fontsize=14)
    plt.plot(x, y, "bo")
    plt.plot(x, predict(x, w, b), '-r')
    plt.show()


if __name__ == '__main__':
    X, Y = np.loadtxt('pizza.txt', skiprows=1, unpack=True)
    W, B = train(X, Y, iterations=20000, lr=0.0001)
    print("\nw=%.3f, b=%.3f" % (W, B))

    print("Prediction: x=%d => y=%.2f" % (20, predict(20, W, B)))
    show_diagram(X, Y, W, B)
