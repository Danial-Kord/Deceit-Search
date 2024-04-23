import random


def naiive_approach(tree):
    target = tree.target
    value = -1
    node = tree.root
    print("Target: ", target)
    while value != target:
        print("Current node: ", node.value)
        # random direction
        direction = random.choice([True, False])  # True is right, False is left
        answers = 0
        print("Is the target to the {}?".format("right" if direction else "left"))
        for i in range(2 * numer_of_lies + 1):
            answer = tree.direction(node, direction)
            print("Answer: ", answer)
            answers += 1 if answer else -1
        go_right = False
        if answers >= 0:
            go_right = direction
        else:
            go_right = not direction
        if go_right:
            print("Go right")
            node = node.right
        else:
            print("Go left")
            node = node.left
        value = node.value

    print("Target found!", value)


from structure import BinaryTree

numer_of_lies = 4

# Test
tree = BinaryTree(10, max_value=50, number_of_lies=numer_of_lies)
for value in tree:
    print(value)


tree.print_tree(tree.root)

tree.draw()

print("-"*50)
print("Naiive approach:")
naiive_approach(tree)
print("End of naiive approach")
print("-"*50)


