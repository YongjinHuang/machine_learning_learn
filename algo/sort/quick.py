import random


def choose_pivot(left, right):
    """
    Function to choose pivot point
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    # Pick 3 random numbers within the range of the list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    # Return their median
    return max(min(i1, i2), min(max(i1, i2), i3))


def quick_sort(lst):
    def partition(left, right):
        pivot_idx = choose_pivot(left, right)
        # pivot_idx = left + (right - left) // 2
        lst[pivot_idx], lst[right] = lst[right], lst[pivot_idx]
        pivot = lst[right]
        i = left - 1
        for j in range(left, right):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[right] = lst[right], lst[i + 1]
        return i + 1

    def quick_sort_recursively(left, right):
        if left < right:
            pivot_idx = partition(left, right)
            quick_sort_recursively(left, pivot_idx - 1)
            quick_sort_recursively(pivot_idx + 1, right)

    quick_sort_recursively(0, len(lst) - 1)


# Driver code to test above
if __name__ == '__main__':
    lst = [5, 4, 2, 1, 3]
    quick_sort(lst)

    # Printing Sorted list
    print("Sorted list: ", lst)
