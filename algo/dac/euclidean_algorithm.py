def euclidean_algorithm(x, y):
    return x if y == 0 else euclidean_algorithm(y, x % y)


if __name__ == '__main__':
    print(euclidean_algorithm(1071, 462))
    print(euclidean_algorithm(462, 1071))
