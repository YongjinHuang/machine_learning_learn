def recursive_multiply(x, y):
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return (recursive_multiply(x, y // 2) << 1) + (x if y & 1 > 0 else 0)


print(recursive_multiply(5, 33333))
