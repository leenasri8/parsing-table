# first_follow.py
# FIRST and FOLLOW computation for Context Free Grammar

from collections import defaultdict


# ---------------------------
# FIRST Computation
# ---------------------------
def compute_first(grammar):
    FIRST = defaultdict(set)

    def first(symbol):
        # If terminal → FIRST is itself
        if symbol not in grammar:
            return {symbol}

        if FIRST[symbol]:
            return FIRST[symbol]

        for production in grammar[symbol]:
            if production == 'ε':
                FIRST[symbol].add('ε')
            else:
                for char in production:
                    char_first = first(char)
                    FIRST[symbol].update(char_first - {'ε'})

                    if 'ε' not in char_first:
                        break
                else:
                    FIRST[symbol].add('ε')

        return FIRST[symbol]

    for non_terminal in grammar:
        first(non_terminal)

    return FIRST


# ---------------------------
# FOLLOW Computation
# ---------------------------
def compute_follow(grammar, FIRST, start_symbol):
    FOLLOW = defaultdict(set)
    FOLLOW[start_symbol].add('$')

    changed = True

    while changed:
        changed = False

        for nt in grammar:
            for production in grammar[nt]:

                for i, symbol in enumerate(production):
                    if symbol in grammar:

                        # Case 1 → Symbol followed by something
                        if i + 1 < len(production):
                            next_symbol = production[i + 1]
                            before = len(FOLLOW[symbol])

                            if next_symbol in grammar:
                                FOLLOW[symbol].update(FIRST[next_symbol] - {'ε'})
                            else:
                                FOLLOW[symbol].add(next_symbol)

                            if len(FOLLOW[symbol]) > before:
                                changed = True

                        # Case 2 → Symbol at end
                        if i + 1 == len(production) or \
                           (production[i + 1] in grammar and 'ε' in FIRST[production[i + 1]]):

                            before = len(FOLLOW[symbol])
                            FOLLOW[symbol].update(FOLLOW[nt])

                            if len(FOLLOW[symbol]) > before:
                                changed = True

    return FOLLOW


# ---------------------------
# Print Sets
# ---------------------------
def print_sets(sets, title):
    print("\n" + title)
    print("=" * 30)
    for symbol in sets:
        print(f"{symbol} : {{ {', '.join(sets[symbol])} }}")


# ---------------------------
# Example Grammar
# ---------------------------
if __name__ == "__main__":

    # Example Grammar
    grammar = {
        "E": ["TR"],
        "R": ["+TR", "ε"],
        "T": ["FY"],
        "Y": ["*FY", "ε"],
        "F": ["(E)", "i"]
    }

    start_symbol = "E"

    FIRST = compute_first(grammar)
    FOLLOW = compute_follow(grammar, FIRST, start_symbol)

    print_sets(FIRST, "FIRST Sets")
    print_sets(FOLLOW, "FOLLOW Sets")