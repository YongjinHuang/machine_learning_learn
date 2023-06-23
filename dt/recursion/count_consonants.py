def is_consonants(letter):
    return letter.isalpha() and letter not in 'aeiouAEIOU'


def count_consonants_iterative(input_str):
    res = 0
    for c in input_str:
        if is_consonants(c):
            res += 1
    return res


def count_consonants_recursive(input_str):
    if input_str == '':
        return 0
    return count_consonants_recursive(input_str[1:]) + (1 if is_consonants(input_str[0]) else 0)


print(count_consonants_iterative("Welcome to Educative!"))
print(count_consonants_recursive("Welcome to Educative!"))
