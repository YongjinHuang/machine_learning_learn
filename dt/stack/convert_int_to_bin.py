from dt.stack.stack import Stack


def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    stack = Stack()
    while dec_num:
        stack.push(dec_num % 2)
        dec_num //= 2
    bin_num = ""
    while not stack.is_empty():
        bin_num += str(stack.pop())
    return bin_num


print(convert_int_to_bin(32))
print(convert_int_to_bin(31))
print(convert_int_to_bin(0))
