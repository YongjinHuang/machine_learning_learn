from dt.stack.stack import Stack


def is_match(param, char):
    if param == "(" and char == ")":
        return True
    if param == "[" and char == "]":
        return True
    if param == "{" and char == "}":
        return True
    return False


def is_paren_balanced(paren_string):
    stack = Stack()

    for char in paren_string:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or not is_match(stack.pop(), char):
                return False

    return stack.is_empty()


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))
