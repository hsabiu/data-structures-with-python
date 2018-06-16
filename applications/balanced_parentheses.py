from implementations.Stack import LinkedListStack


def parse_parentheses(expression):
    """Function to check for balanced parentheses in an expression using stack data structure"""

    stack = LinkedListStack()
    expression = expression.split(" ")
    parentheses = {")": "(", "}": "{", "]": "["}

    for ch in expression:
        if ch in ["(", "{", "["]:
            stack.push(ch)
        elif ch in [")", "}", "]"]:
            stack_top = stack.pop()
            if not parentheses[ch] == stack_top:
                return False

    return stack.is_empty()


if __name__ == '__main__':

    print("Correct parenthesis, should return True...")
    print("===> Function call return:", parse_parentheses("{ ( [ ] ) }"))
    print("")

    print("Incorrect parenthesis, should return False...")
    print("===> Function call return:", parse_parentheses("{ ( [ ) ] ) }"))
    print("")

    print("Expression with correct parenthesis, should return True...")
    print("===> Function call return:", parse_parentheses("( 2 + ( ( 3 + 4 ) * ( 5 * 6 ) ) )"))
    print("")

    print("Expression with incorrect parenthesis, should return False...")
    print("===> Function call return:", parse_parentheses("( 2 + ( ( 3 + 4 ( * ( 5 * 6 ) ) )"))