from algo.stack.stack import Stack


def is_paren_balanced(paren_string):
    stack = Stack()
    a = {1: 2, 3: 4}
    a.get(1)

    for char in paren_string:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


print(is_paren_balanced("((()))"))
print(is_paren_balanced("(()"))
print(is_paren_balanced("())"))
