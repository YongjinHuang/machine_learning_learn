import numpy as np

from ml.sigmoid import mnist


# Applying Logistic Regression
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Calling the predict() function
def classify(x, w):
    return np.round(forward(x, w))


def log_loss(x, y, w):
    y_hat = forward(x, w)
    return -np.average(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))


# Mean Squared Error Loss
def mse_loss(x, y, w):
    return np.average((forward(x, w) - y) ** 2)


def gradient(x, y, w):
    y_hat = forward(x, w)
    return np.matmul(x.T, y_hat - y) / x.shape[0]


# Basically doing prediction but named forward as its performing forward propagation
def forward(x, w):
    weighted_sum = np.matmul(x, w)
    return sigmoid(weighted_sum)


def train(x, y, iterations, lr):
    w = np.zeros((x.shape[1], 1))
    for i in range(iterations):
        w -= lr * gradient(x, y, w)
        print(f'Iteration: {i}, Loss: {log_loss(x, y, w)}')
    return w


def test(x, y, w):
    total_examples = x.shape[0]
    correct_results = np.sum(classify(x, w) == y)
    success_percent = correct_results / total_examples * 100
    print(f'Total Examples: {total_examples}, Correct Results: {correct_results}, Success Percent: {success_percent}')


# x1, x2, x3, y = np.loadtxt('police.txt', skiprows=1, unpack=True)
# x = np.column_stack((np.ones(x1.size), x1, x2, x3))
# y = y.reshape(-1, 1)
# w = train(x, y, iterations=10000, lr=0.001)
#
# test(x, y, w)
# print(w)
if __name__ == '__main__':

    # Prepend a column of 1s to the matrix of inputs
    # Load the images and labels from the mnist dataset
    x = mnist.prepend_bias(mnist.load_images('../../data/mnist/train-images-idx3-ubyte.gz'))
    raw_y = mnist.load_labels('../../data/mnist/train-labels-idx1-ubyte.gz')
    x_test = mnist.prepend_bias(mnist.load_images('../../data/mnist/t10k-images-idx3-ubyte.gz'))
    raw_y_test = mnist.load_labels('../../data/mnist/t10k-labels-idx1-ubyte.gz')
    for digit in range(10):
        print(f"{digit} vs all")
        # Encode the labels into a matrix of 0s and 1s
        y = mnist.encode_digits(raw_y, digit=digit)
        # Train the model
        w = train(x, y, iterations=100, lr=1e-5)
        y_test = mnist.encode_digits(raw_y_test, digit=digit)
        # Test the model
        test(x_test, y_test, w)
