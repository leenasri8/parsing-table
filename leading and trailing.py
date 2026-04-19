from collections import defaultdict

# Grammar (modify if needed)
grammar = {
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'i']
}

leading = defaultdict(set)
trailing = defaultdict(set)

# Function to compute LEADING
def compute_leading():
    changed = True
    while changed:
        changed = False
        for head in grammar:
            for prod in grammar[head]:
                # Rule 1: first symbol is terminal
                if prod[0] not in grammar:
                    if prod[0] not in leading[head]:
                        leading[head].add(prod[0])
                        changed = True
                
                # Rule 2: first symbol is non-terminal
                else:
                    for sym in leading[prod[0]]:
                        if sym not in leading[head]:
                            leading[head].add(sym)
                            changed = True

                # Rule 3: terminal after non-terminal
                if len(prod) > 1 and prod[0] in grammar and prod[1] not in grammar:
                    if prod[1] not in leading[head]:
                        leading[head].add(prod[1])
                        changed = True

# Function to compute TRAILING
def compute_trailing():
    changed = True
    while changed:
        changed = False
        for head in grammar:
            for prod in grammar[head]:
                # Rule 1: last symbol is terminal
                if prod[-1] not in grammar:
                    if prod[-1] not in trailing[head]:
                        trailing[head].add(prod[-1])
                        changed = True
                
                # Rule 2: last symbol is non-terminal
                else:
                    for sym in trailing[prod[-1]]:
                        if sym not in trailing[head]:
                            trailing[head].add(sym)
                            changed = True

                # Rule 3: terminal before non-terminal
                if len(prod) > 1 and prod[-1] in grammar and prod[-2] not in grammar:
                    if prod[-2] not in trailing[head]:
                        trailing[head].add(prod[-2])
                        changed = True

# Run computations
compute_leading()
compute_trailing()

# Output
print("LEADING:")
for nt in grammar:
    print(f"{nt} : {leading[nt]}")

print("\nTRAILING:")
for nt in grammar:
    print(f"{nt} : {trailing[nt]}")