def insertion_sort(lst):
    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Move elements of lst[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


# Driver code to test above
if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    insertion_sort(lst)  # Calling insertion sort function

    print("Sorted list is: ", lst)
