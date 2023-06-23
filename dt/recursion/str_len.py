def str_len_iterative(input_str):
    res = 0
    for _ in input_str:
        res += 1
    return res


def str_len_recursive(input_str):
    if input_str == '':
        return 0
    return 1 + str_len_recursive(input_str[1:])


input_str = "LucidProgramming"

print(str_len_iterative(input_str))
print(str_len_recursive(input_str))
