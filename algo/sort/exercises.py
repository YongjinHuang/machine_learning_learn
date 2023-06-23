def find_two_sum(lst, n):
    cur = set()
    for num in lst:
        if n - num in cur:
            return [n - num, num]
        cur.add(num)
    return None


def search_in_sorted_matrix(matrix, target):
    row, column = len(matrix) - 1, 0
    while row >= 0 and column < len(matrix[0]):
        num = matrix[row][column]
        if num == target:
            return True
        elif num > target:
            row -= 1
        else:
            column += 1
    return False


def sort_binary_list(lst):
    j = -1
    for i in range(len(lst)):
        if lst[i] < 1:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
    return lst
