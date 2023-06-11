import gzip
import struct
import numpy as np
import matplotlib.pyplot as plt


def load_images(filename):
    # Open and unzip the file of images
    with gzip.open(filename, 'rb') as f:
        # Read the header information into a bunch of variables
        _ignored, n_images, columns, rows = struct.unpack('>IIII', f.read(16))
        # Read all the pixels into a long NumPy array
        all_pixels = np.frombuffer(f.read(), dtype=np.uint8)
        # Reshape the array into a matrix where each line is an image
        return all_pixels.reshape(n_images, columns * rows)


def prepend_bias(x):
    # Insert a column of 1s in the position 0 of the matrix x
    # axis=1 stands for columns, axis=0 stands for lines
    return np.insert(x, 0, 1, axis=1)


def load_labels(filenames):
    with gzip.open(filenames, 'rb') as f:
        # Skip the header bytes
        f.read(8)
        # Read all the labels into a list
        all_labels = f.read()
        # Reshape the list into a one-column matrix
        return np.frombuffer(all_labels, dtype=np.uint8).reshape(-1, 1)


def one_hot_encode(y, n_classes=10):
    # Create a matrix of 0s with as many lines as y and 10 columns
    encoded = np.zeros((y.shape[0], n_classes))
    # For each line of the matrix, set the column y[i] to 1
    encoded[np.arange(y.shape[0]), y] = 1
    return encoded


def encode_digits(y, digit=5):
    return (y == digit).astype(int)


if __name__ == '__main__':
    x = load_images('../../data/mnist/train-images-idx3-ubyte.gz')
    y = load_labels('../../data/mnist/train-labels-idx1-ubyte.gz').flatten()
    digits = x[y == 7]
    np.random.shuffle(digits)

    rows, columns = 3, 15
    fig, axes = plt.subplots(nrows=rows, ncols=columns, dpi=800)
    for i in range(rows):
        for j in range(columns):
            axes[i, j].axis('off')
            axes[i, j].imshow(digits[i * columns + j].reshape(28, 28), cmap='gray')
    plt.show()
