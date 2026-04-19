from collections import defaultdict

# Grammar (Augmented)
grammar = {
    "S'": ["S"],
    "S": ["CC"],
    "C": ["cC", "d"]
}

# Function: Closure
def closure(items):
    closure_set = set(items)

    while True:
        new_items = set(closure_set)

        for item in closure_set:
            head, body = item.split("->")
            dot_pos = body.find('.')

            # If dot is not at end
            if dot_pos < len(body) - 1:
                symbol = body[dot_pos + 1]

                # If symbol is non-terminal
                if symbol in grammar:
                    for prod in grammar[symbol]:
                        new_item = symbol + "->." + prod
                        new_items.add(new_item)

        if new_items == closure_set:
            break
        closure_set = new_items

    return closure_set

# Function: GOTO
def goto(items, symbol):
    moved_items = set()

    for item in items:
        head, body = item.split("->")
        dot_pos = body.find('.')

        if dot_pos < len(body) - 1 and body[dot_pos + 1] == symbol:
            # Move dot
            new_body = body[:dot_pos] + symbol + '.' + body[dot_pos + 2:]
            moved_items.add(head + "->" + new_body)

    return closure(moved_items)

# Initial Item
start_item = ["S'->.S"]

# Compute Canonical Collection
C = []
C.append(closure(start_item))

symbols = ['S', 'C', 'c', 'd']

i = 0
while i < len(C):
    for sym in symbols:
        g = goto(C[i], sym)
        if g and g not in C:
            C.append(g)
    i += 1

# Print LR(0) Items
for idx, state in enumerate(C):
    print(f"\nI{idx}:")
    for item in state:
        print(item)