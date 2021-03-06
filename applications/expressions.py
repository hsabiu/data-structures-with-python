import operator
from implementations.Stack import LinkedListStack


def evaluate_postfix(expression):
    """Function to evaluate an expression represented in postfix
    notation using stack data structure"""

    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    stack = LinkedListStack()

    expression = expression.split(" ")

    for ch in expression:
        if ch in ["+", "-", "*", "/"]:
            second_operand = stack.pop()
            first_operand = stack.pop()
            op_result = ops[ch](first_operand, second_operand)
            stack.push(op_result)
        else:
            stack.push(float(ch))

    return stack.peek()


def evaluate_prefix(expression):
    """A function to evaluate an expression represented in prefix
    notation using Stack data structure"""
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
    stack = LinkedListStack()

    expression = expression.split(" ")

    for ch in reversed(expression):
        if ch in ["+", "-", "*", "/"]:
            first_operand = stack.pop()
            second_operand = stack.pop()
            op_result = ops[ch](first_operand, second_operand)
            stack.push(op_result)
        else:
            stack.push(float(ch))

    return stack.peek()


if __name__ == '__main__':

    postfix_notation = "1 2 + 3 4 + +"
    postfix_evaluation_result = evaluate_postfix(postfix_notation)
    print(f"The postfix expression: {postfix_notation} = ", postfix_evaluation_result)

    prefix_notation = "+ + 1 2 + 3 4"
    prefix_evaluation_result = evaluate_prefix(prefix_notation)
    print(f"The prefix expression: {prefix_notation} = ", prefix_evaluation_result)


