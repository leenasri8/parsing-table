# Function: precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# INFIX → POSTFIX
def infix_to_postfix(expr):
    stack = []
    output = []

    for ch in expr:
        if ch.isalnum():  # operand
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(ch):
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# INFIX → PREFIX
def infix_to_prefix(expr):
    # reverse expression
    expr = expr[::-1]

    # swap brackets
    expr = list(expr)
    for i in range(len(expr)):
        if expr[i] == '(':
            expr[i] = ')'
        elif expr[i] == ')':
            expr[i] = '('

    expr = ''.join(expr)

    # postfix of modified expression
    postfix = infix_to_postfix(expr)

    # reverse postfix → prefix
    return postfix[::-1]


# MAIN
expr = input("Enter infix expression: ")

postfix = infix_to_postfix(expr)
prefix = infix_to_prefix(expr)

print("Postfix :", postfix)
print("Prefix  :", prefix)