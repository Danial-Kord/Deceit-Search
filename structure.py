import random
import networkx as nx
import matplotlib.pyplot as plt


# Node class
class Node:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None
        self.pos = None  # Position will be set during drawing

    # Print node
    def print_node(self):
        if self.right is not None and self.left is not None:
            print(f"Value: {self.value}, Depth: {self.depth}, left: {self.left.value}, right: {self.right.value}" )
        elif self.right is None and self.left is not None:
            print(f"Value: {self.value}, Depth: {self.depth}, left: {self.left.value}, right: None" )
        elif self.left is None and self.right is not None:
            print(f"Value: {self.value}, Depth: {self.depth}, left: None, right: {self.right.value}" )
        else:
            print(f"Value: {self.value}, Depth: {self.depth}, left: None, right: None" )


# Binary tree class
class BinaryTree:
    def __init__(self, size, max_value=100, number_of_lies=0):
        self.root = None
        values = random.sample(range(max_value), size)
        self.target = random.choice(values) #our target
        self.number_of_lies = number_of_lies
        self.question_number = 0
        self.lie_places = random.sample(range(size.bit_length() * (2 * number_of_lies + 1)), number_of_lies)
        print(values)
        for value in values:
            self.insert(value)


    def direction(self, node, is_right = False):
        tell_lie = False
        if self.question_number in self.lie_places:
            tell_lie = True
        self.question_number += 1
        if node.value <= self.target:
            if tell_lie:
                return not (is_right is True)
            return is_right is True
        else:
            if tell_lie:
                return not (is_right is False)
            return is_right is False

    # Insert value if root is None or call recursive insert
    def insert(self, value):
        depth = 0
        if self.root is None:
            self.root = Node(value, depth)
        else:
            self._insert_rec(self.root, value, depth+1)

    # Recursive insert until a leaf is found
    def _insert_rec(self, node, value, depth):
        if value < node.value:
            if node.left is None:
                node.left = Node(value, depth)
            else:
                self._insert_rec(node.left, value, depth+1)
        else:
            if node.right is None:
                node.right = Node(value, depth)
            else:
                self._insert_rec(node.right, value, depth+1)

    def __iter__(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield node.value
            yield from self._in_order_traversal(node.right)


    # Print tree
    def print_tree(self, node = None):
        node.print_node()
        if node.left is not None:
            self.print_tree(node.left)
        if node.right is not None:
            self.print_tree(node.right)

    # draw tree
    def draw(self):
        G = nx.DiGraph()
        labels = {}
        pos = {}
        self._add_edges(self.root, G, labels, pos, 0, 0)
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color='skyblue')
        plt.show()

    # adding visual edges to the tree
    def _add_edges(self, node, G, labels, pos, x, depth):
        if node:
            node_id = id(node)  # Unique identifier for each node
            node.pos = (x, -depth)
            G.add_node(node_id)
            labels[node_id] = node.value
            pos[node_id] = node.pos
            if node.left:
                G.add_edge(node_id, id(node.left))
                self._add_edges(node.left, G, labels, pos, x - 1 / (2 ** (depth + 1)), depth + 1)
            if node.right:
                G.add_edge(node_id, id(node.right))
                self._add_edges(node.right, G, labels, pos, x + 1 / (2 ** (depth + 1)), depth + 1)

