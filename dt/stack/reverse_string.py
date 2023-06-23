from dt.stack.stack import Stack


def reverse_string(input_str):
    stack = Stack()
    for char in input_str:
        stack.push(char)
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


print(reverse_string("Hello"))
print(reverse_string("World"))
print(reverse_string("Hello World"))
