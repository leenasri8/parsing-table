stack = []
input_string = input("Enter input string: ")
i = 0

def reduce_stack():
    global stack
    changed = True
    while changed:
        changed = False

        # id → E
        if len(stack) >= 2 and stack[-2] == 'i' and stack[-1] == 'd':
            stack = stack[:-2]
            stack.append('E')
            print(stack, "\tReduce id→E")
            changed = True

        # E+E → E
        elif len(stack) >= 3 and stack[-3:] == ['E', '+', 'E']:
            stack = stack[:-3]
            stack.append('E')
            print(stack, "\tReduce E+E→E")
            changed = True

        # E*E → E
        elif len(stack) >= 3 and stack[-3:] == ['E', '*', 'E']:
            stack = stack[:-3]
            stack.append('E')
            print(stack, "\tReduce E*E→E")
            changed = True

        # (E) → E
        elif len(stack) >= 3 and stack[-3:] == ['(', 'E', ')']:
            stack = stack[:-3]
            stack.append('E')
            print(stack, "\tReduce (E)→E")
            changed = True

print("\nStack\t\tAction")

while i < len(input_string):
    # SHIFT
    stack.append(input_string[i])
    print(stack, "\tShift")
    i += 1

    # REDUCE
    reduce_stack()

# Final check
if stack == ['E']:
    print("\nString Accepted")
else:
    print("\nString Rejected")