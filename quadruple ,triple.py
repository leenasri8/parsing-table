temp_count = 1

# Generate new temporary variable
def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

# Check operator
def is_operator(c):
    return c in ['+', '-', '*', '/']

# Generate Quadruple & Triple
def generate_code(postfix):
    stack = []
    quadruple = []
    triple = []

    for ch in postfix:
        if not is_operator(ch):  # operand
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            temp = new_temp()

            # Quadruple: (op, arg1, arg2, result)
            quadruple.append((ch, op1, op2, temp))

            # Triple: (op, arg1, arg2)
            triple.append((ch, op1, op2))

            stack.append(temp)

    return quadruple, triple


# MAIN
postfix = input("Enter postfix expression: ")

quad, trip = generate_code(postfix)

print("\nQuadruple Representation:")
for i, q in enumerate(quad):
    print(f"{i}: {q}")

print("\nTriple Representation:")
for i, t in enumerate(trip):
    print(f"{i}: {t}")