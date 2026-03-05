# regex_to_nfa.py
# Conversion of Regular Expression to NFA using Thompson's Construction

class State:
    def __init__(self):
        self.transitions = {}   # symbol -> list of states
        self.epsilon = []       # epsilon transitions


class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def basic_nfa(symbol):
    start = State()
    end = State()
    start.transitions.setdefault(symbol, []).append(end)
    return NFA(start, end)


def concatenate(nfa1, nfa2):
    nfa1.end.epsilon.append(nfa2.start)
    return NFA(nfa1.start, nfa2.end)


def union(nfa1, nfa2):
    start = State()
    end = State()

    start.epsilon.extend([nfa1.start, nfa2.start])
    nfa1.end.epsilon.append(end)
    nfa2.end.epsilon.append(end)

    return NFA(start, end)


def kleene_star(nfa):
    start = State()
    end = State()

    start.epsilon.extend([nfa.start, end])
    nfa.end.epsilon.extend([nfa.start, end])

    return NFA(start, end)


def precedence(op):
    if op == '*':
        return 3
    elif op == '.':
        return 2
    elif op == '|':
        return 1
    return 0


def add_concat(regex):
    result = ""
    for i in range(len(regex)):
        result += regex[i]
        if i + 1 < len(regex):
            if regex[i] not in "(|" and regex[i+1] not in ")*|":
                result += "."
    return result


def infix_to_postfix(regex):
    stack = []
    postfix = ""

    for char in regex:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix


def regex_to_nfa(regex):
    regex = add_concat(regex)
    postfix = infix_to_postfix(regex)

    stack = []

    for char in postfix:
        if char.isalnum():
            stack.append(basic_nfa(char))
        elif char == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            stack.append(concatenate(nfa1, nfa2))
        elif char == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            stack.append(union(nfa1, nfa2))
        elif char == '*':
            nfa = stack.pop()
            stack.append(kleene_star(nfa))

    return stack.pop()


def print_nfa(nfa):
    visited = set()
    stack = [nfa.start]

    print("\nNFA Transitions:")

    while stack:
        state = stack.pop()
        if id(state) in visited:
            continue

        visited.add(id(state))

        for symbol, states in state.transitions.items():
            for s in states:
                print(f"{id(state)} -- {symbol} --> {id(s)}")
                stack.append(s)

        for s in state.epsilon:
            print(f"{id(state)} -- ε --> {id(s)}")
            stack.append(s)


if __name__ == "__main__":
    regex = input("Enter Regular Expression: ")
    nfa = regex_to_nfa(regex)
    print_nfa(nfa)