# Predictive Parsing Table Generator (LL(1))

# ---------- INPUT GRAMMAR ----------
# Example Grammar
# E  -> T E'
# E' -> + T E' | ε
# T  -> F T'
# T' -> * F T' | ε
# F  -> ( E ) | id

grammar = {
    "E": ["T E'"],
    "E'": ["+ T E'", "ε"],
    "T": ["F T'"],
    "T'": ["* F T'", "ε"],
    "F": ["( E )", "id"]
}

# ---------- FIRST SET ----------
FIRST = {
    "E": {"(", "id"},
    "E'": {"+", "ε"},
    "T": {"(", "id"},
    "T'": {"*", "ε"},
    "F": {"(", "id"}
}

# ---------- FOLLOW SET ----------
FOLLOW = {
    "E": {")", "$"},
    "E'": {")", "$"},
    "T": {"+", ")", "$"},
    "T'": {"+", ")", "$"},
    "F": {"*", "+", ")", "$"}
}

# ---------- TERMINALS ----------
terminals = ["id", "+", "*", "(", ")", "$"]

# ---------- CREATE PARSING TABLE ----------
parsing_table = {}

for non_terminal in grammar:
    parsing_table[non_terminal] = {}
    for terminal in terminals:
        parsing_table[non_terminal][terminal] = ""

for non_terminal in grammar:
    for production in grammar[non_terminal]:
        first_symbol = production.split()[0]

        # If first symbol is terminal
        if first_symbol not in grammar:
            parsing_table[non_terminal][first_symbol] = production

        else:
            for symbol in FIRST[first_symbol]:
                if symbol != "ε":
                    parsing_table[non_terminal][symbol] = production

        # If epsilon production
        if production == "ε":
            for follow_symbol in FOLLOW[non_terminal]:
                parsing_table[non_terminal][follow_symbol] = production

# ---------- DISPLAY TABLE ----------
print("\nPredictive Parsing Table\n")

print("{:10}".format(" "), end="")
for t in terminals:
    print("{:10}".format(t), end="")
print()

for nt in parsing_table:
    print("{:10}".format(nt), end="")
    for t in terminals:
        print("{:10}".format(parsing_table[nt][t]), end="")
    print()
