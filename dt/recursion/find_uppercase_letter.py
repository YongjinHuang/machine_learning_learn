def find_uppercase_letter_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]

    return "No uppercase letter found"


def find_uppercase_letter_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase letter found"
    return find_uppercase_letter_recursive(input_str, idx + 1)


input_str_1 = "bradeProgramming"
input_str_2 = "BradeProgramming"
input_str_3 = "bradeprogramming"
testcases = [input_str_1, input_str_2, input_str_3]

for testcase in testcases:
    print(find_uppercase_letter_iterative(testcase) == find_uppercase_letter_recursive(testcase))
