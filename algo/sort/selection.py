def selection_sort(lst):
    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in remaining unsorted lst
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        # swap the found minimum element with the first element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)
