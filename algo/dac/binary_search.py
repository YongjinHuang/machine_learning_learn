def binary_search(arr, low, high, x):
    if low <= high:
        middle = low + (high - low) // 2
        if arr[middle] == x:
            return True
        if arr[middle] < x:
            return binary_search(arr, middle + 1, high, x)
        return binary_search(arr, low, middle - 1, x)
    return -1


if __name__ == '__main__':
    lst = [2, 4, 7, 25, 60]
    key = 25  # to find, feel free to change this

    result = binary_search(lst, 0, len(lst) - 1, key)

    if result == -1:
        print("Element is not present in the list")
    else:
        print("Element is present at index: ", result)
