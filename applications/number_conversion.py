from implementations.Stack import LinkedListStack


def convert_base(numb, base):
    """Convert decimal numbers to any base using the repeated division"""

    digits = "0123456789ABCDEF"
    stack = LinkedListStack()

    while numb > 0:
        stack.push(numb % base)
        numb = numb // base

    converted = ''
    while not stack.is_empty():
        converted = converted + digits[stack.pop()]

    return converted


if __name__ == '__main__':
    decimal_number = 256
    binary_number = convert_base(decimal_number, 2)
    octal_number = convert_base(decimal_number, 8)
    hexadecimal_number = convert_base(decimal_number, 16)

    print(f"===> Number in decimal = {decimal_number}")
    print(f"===> Number in binary = {binary_number}")
    print(f"===> Number in octal = {octal_number}")
    print(f"===> Number in hexadecimal = {hexadecimal_number}")

