# -------------------------------
# Left Recursion Elimination
# -------------------------------

def remove_left_recursion(grammar):
    new_grammar = {}

    for non_terminal in grammar:
        alpha = []
        beta = []

        for production in grammar[non_terminal]:
            if production.startswith(non_terminal):
                alpha.append(production[len(non_terminal):])
            else:
                beta.append(production)

        if alpha:
            new_non_terminal = non_terminal + "'"
            new_grammar[non_terminal] = []

            for b in beta:
                new_grammar[non_terminal].append(b + new_non_terminal)

            new_grammar[new_non_terminal] = []
            for a in alpha:
                new_grammar[new_non_terminal].append(a + new_non_terminal)

            new_grammar[new_non_terminal].append("ε")
        else:
            new_grammar[non_terminal] = grammar[non_terminal]

    return new_grammar


# -------------------------------
# Left Factoring
# -------------------------------

def left_factoring(grammar):
    new_grammar = {}

    for non_terminal in grammar:
        productions = grammar[non_terminal]
        prefix_dict = {}

        for prod in productions:
            prefix = prod[0]
            prefix_dict.setdefault(prefix, []).append(prod)

        if any(len(v) > 1 for v in prefix_dict.values()):
            new_non_terminal = non_terminal + "'"
            new_grammar[non_terminal] = []
            new_grammar[new_non_terminal] = []

            for prefix in prefix_dict:
                if len(prefix_dict[prefix]) > 1:
                    new_grammar[non_terminal].append(prefix + new_non_terminal)
                    for prod in prefix_dict[prefix]:
                        new_grammar[new_non_terminal].append(prod[1:])
                else:
                    new_grammar[non_terminal].append(prefix_dict[prefix][0])
        else:
            new_grammar[non_terminal] = productions

    return new_grammar


# -------------------------------
# MAIN PROGRAM
# -------------------------------

if __name__ == "__main__":

    print("---- Left Recursion Example ----")
    grammar1 = {
        "A": ["Aα", "β"]
    }

    result1 = remove_left_recursion(grammar1)

    for nt in result1:
        print(nt, "->", " | ".join(result1[nt]))


    print("\n---- Left Factoring Example ----")
    grammar2 = {
        "A": ["ab", "ac"]
    }

    result2 = left_factoring(grammar2)

    for nt in result2:
        print(nt, "->", " | ".join(result2[nt]))