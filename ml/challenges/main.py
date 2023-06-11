import numpy as np

from ml.sigmoid import mnist


# Applying Logistic Regression
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Calling the predict() function
def classify(x, w):
    y_hat = forward(x, w)
    labels = np.argmax(y_hat, axis=1)
    return labels.reshape(-1, 1)


def log_loss(x, y, w):
    y_hat = forward(x, w)
    return -np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)) / x.shape[0]


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


def train(x, y, x_test, y_test, iterations, lr):
    w = np.zeros((x.shape[1], y.shape[1]))
    report(0, x, y, x_test, y_test, w)
    for i in range(iterations):
        w -= lr * gradient(x, y, w)
        report(i+1, x, y, x_test, y_test, w)
    return w


def test(x, y, w):
    total_examples = x.shape[0]
    correct_results = np.sum(classify(x, w) == y)
    success_percent = correct_results / total_examples * 100
    print(f'Total Examples: {total_examples}, Correct Results: {correct_results}, Success Percent: {success_percent}')


def accuracy(x, y, w):
    total_examples = x.shape[0]
    correct_results = np.count_nonzero(classify(x, w) == y)
    return correct_results / total_examples * 100


def report(iteration, x, y, x_test, y_test, w):
    print(f'Iteration: {iteration}')
    print(f'Train Loss: {log_loss(x, y, w)}')
    print(f'Test Accuracy: {accuracy(x_test, y_test, w)}%')


if __name__ == '__main__':
    # Prepend a column of 1s to the matrix of inputs
    # Load the images and labels from the mnist dataset
    y = mnist.one_hot_encode(mnist.load_labels('../../data/mnist/train-labels-idx1-ubyte.gz'), n_classes=10)
    x = mnist.prepend_bias(mnist.load_images('../../data/mnist/train-images-idx3-ubyte.gz'))
    x_test = mnist.prepend_bias(mnist.load_images('../../data/mnist/t10k-images-idx3-ubyte.gz'))
    y_test = mnist.load_labels('../../data/mnist/t10k-labels-idx1-ubyte.gz')
    # Train the model
    w = train(x, y, x_test, y_test, iterations=200, lr=1e-5)
