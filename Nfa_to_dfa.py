# nfa_to_dfa.py
# Conversion of NFA to DFA using Subset Construction Method

from collections import defaultdict, deque


class NFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states


class DFA:
    def __init__(self):
        self.states = []
        self.transitions = {}
        self.start_state = None
        self.final_states = []


def epsilon_closure(states, transitions):
    stack = list(states)
    closure = set(states)

    while stack:
        state = stack.pop()
        for next_state in transitions[state].get('ε', []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return frozenset(closure)


def move(states, symbol, transitions):
    result = set()
    for state in states:
        result.update(transitions[state].get(symbol, []))
    return result


def nfa_to_dfa(nfa):
    dfa = DFA()

    start = epsilon_closure({nfa.start_state}, nfa.transitions)
    dfa.start_state = start

    queue = deque([start])
    visited = set([start])

    while queue:
        current = queue.popleft()
        dfa.states.append(current)

        for symbol in nfa.alphabet:
            next_states = epsilon_closure(
                move(current, symbol, nfa.transitions),
                nfa.transitions
            )

            dfa.transitions[(current, symbol)] = next_states

            if next_states not in visited:
                visited.add(next_states)
                queue.append(next_states)

    for state in dfa.states:
        if any(s in nfa.final_states for s in state):
            dfa.final_states.append(state)

    return dfa


def print_dfa(dfa):
    print("\nDFA States:")
    for state in dfa.states:
        print(state)

    print("\nDFA Transitions:")
    for (state, symbol), next_state in dfa.transitions.items():
        print(f"{state} -- {symbol} --> {next_state}")

    print("\nStart State:")
    print(dfa.start_state)

    print("\nFinal States:")
    for fs in dfa.final_states:
        print(fs)


# Example NFA Input
if __name__ == "__main__":

    states = {'A', 'B', 'C'}
    alphabet = {'0', '1'}

    transitions = defaultdict(dict)
    transitions['A'] = {'0': ['A'], '1': ['A', 'B']}
    transitions['B'] = {'1': ['C']}
    transitions['C'] = {}

    start_state = 'A'
    final_states = {'C'}

    nfa = NFA(states, alphabet, transitions, start_state, final_states)

    dfa = nfa_to_dfa(nfa)
    print_dfa(dfa)