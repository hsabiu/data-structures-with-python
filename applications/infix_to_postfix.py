from implementations.Stack import LinkedListStack


def convert_to_postfix(infix_expr):
    stack = LinkedListStack()

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    infix_expr = infix_expr.split()
    postfix_expr = ''

    for ch in infix_expr:
        if ch not in ['(', ')', '+', '-', '*', '/']:
            postfix_expr = postfix_expr + ch
        elif ch is '(':
            stack.push(ch)
        elif ch is ')':
            top = stack.pop()
            while top != '(':
                postfix_expr = postfix_expr + top
                top = stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != '(' and precedence[stack.peek()] >= precedence[ch]:
                postfix_expr = postfix_expr + stack.pop()
            stack.push(ch)

    while not stack.is_empty():
        postfix_expr = postfix_expr + stack.pop()

    return postfix_expr


if __name__ == '__main__':
    # infix = 'A * B + C * D'
    infix = '( A + B ) * ( C + D )'
    # infix = '( A + B ) * C'
    # infix = 'A + B * C'
    postfix = convert_to_postfix(infix)

    print(postfix)