temp_count = 1

def new_temp():
    global temp_count
    temp = f"R{temp_count}"   # Register name
    temp_count += 1
    return temp

def generate_code(postfix):
    stack = []

    print("\nGenerated Code:\n")

    for ch in postfix:
        if ch.isalnum():   # operand
            stack.append(ch)
        else:              # operator
            op2 = stack.pop()
            op1 = stack.pop()

            reg = new_temp()

            print(f"MOV {reg}, {op1}")
            if ch == '+':
                print(f"ADD {reg}, {op2}")
            elif ch == '-':
                print(f"SUB {reg}, {op2}")
            elif ch == '*':
                print(f"MUL {reg}, {op2}")
            elif ch == '/':
                print(f"DIV {reg}, {op2}")

            stack.append(reg)

# MAIN
postfix = input("Enter postfix expression: ")
generate_code(postfix)