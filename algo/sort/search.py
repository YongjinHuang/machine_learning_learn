def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1


def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if lst[middle] == key:
            return middle
        if lst[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    return -1


# Driver code to test above
if __name__ == '__main__':

    lst = [5, 4, 1, 0, 5, 95, 4, -100, 200, 0]
    key = 95

    index = linear_search(lst, key)
    if index != -1:
        print("Key:", key, "is found at index:", index)
    else:
        print(key, " is not found in the list.")
