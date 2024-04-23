from structure import BinaryTree


# Test
tree = BinaryTree(10, max_value=50)
for value in tree:
    print(value)


tree.print_tree(tree.root)

tree.draw()
