# Basic Blocks with GEN and KILL sets
blocks = {
    "B1": {"gen": {"d1", "d2"}, "kill": {"d3"}},
    "B2": {"gen": {"d3"}, "kill": {"d2"}},
    "B3": {"gen": {"d4"}, "kill": set()}
}

# Control Flow Graph (CFG)
cfg = {
    "B1": ["B2"],
    "B2": ["B3"],
    "B3": []
}

# Initialize IN and OUT
IN = {b: set() for b in blocks}
OUT = {b: set() for b in blocks}

changed = True

while changed:
    changed = False
    for b in blocks:
        # IN[b] = union of OUT[pred]
        new_in = set()
        for p in cfg:
            if b in cfg[p]:
                new_in |= OUT[p]

        # OUT[b] = GEN[b] ∪ (IN[b] - KILL[b])
        new_out = blocks[b]["gen"] | (new_in - blocks[b]["kill"])

        if new_in != IN[b] or new_out != OUT[b]:
            IN[b] = new_in
            OUT[b] = new_out
            changed = True

# Output
print("Reaching Definitions:\n")

for b in blocks:
    print(f"{b}:")
    print(" IN  =", IN[b])
    print(" OUT =", OUT[b])
    print()