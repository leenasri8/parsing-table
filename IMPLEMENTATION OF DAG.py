class Node:
    def __init__(self, op=None, left=None, right=None, value=None):
        self.op = op
        self.left = left
        self.right = right
        self.value = value   # for operands

    def __repr__(self):
        if self.value:
            return self.value
        return f"({self.left} {self.op} {self.right})"


class DAG:
    def __init__(self):
        self.nodes = []

    # Check if node already exists (common subexpression)
    def find_node(self, op, left, right):
        for node in self.nodes:
            if node.op == op and node.left == left and node.right == right:
                return node
        return None

    def get_leaf(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        node = Node(value=value)
        self.nodes.append(node)
        return node

    def make_node(self, op, left, right):
        existing = self.find_node(op, left, right)
        if existing:
            return existing   # reuse node (optimization)

        node = Node(op, left, right)
        self.nodes.append(node)
        return node


# Build DAG from postfix expression
def build_dag(postfix):
    dag = DAG()
    stack = []

    for ch in postfix:
        if ch.isalnum():  # operand
            stack.append(dag.get_leaf(ch))
        else:             # operator
            right = stack.pop()
            left = stack.pop()
            node = dag.make_node(ch, left, right)
            stack.append(node)

    return dag, stack[-1]


# MAIN
postfix = input("Enter postfix expression: ")

dag, root = build_dag(postfix)

print("\nDAG Nodes:")
for node in dag.nodes:
    print(node)

print("\nOptimized Expression (from DAG):")
print(root)