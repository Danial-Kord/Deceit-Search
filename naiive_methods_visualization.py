import random


#Keep asking each quesrtion for 2*E+1 times
def naiive_approach(number_of_lies = 4):
    target = tree.target
    value = -1
    node = tree.root
    print("Target: ", target)
    number_of_questions = 0
    while value != target:
        number_of_questions += 1
        print("Current node: ", node.value)
        # random direction
        direction = random.choice([True, False])  # True is right, False is left
        answers = 0
        print("Is the target to the {}?".format("right" if direction else "left"))
        for i in range(2 * number_of_lies + 1):
            number_of_questions += 1
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
    return number_of_questions

# Keep tracking the number of questions asked
def historical_naiive_approach(E = 4):
    target = tree.target
    value = -1
    node = tree.root
    print("Target: ", target)
    number_of_questions = 0
    total_received_lies = 0
    number_of_lies = E
    while value != target:
        number_of_questions += 1
        print("Current node: ", node.value)
        # random direction
        direction = random.choice([True, False])  # True is right, False is left
        answers = 0
        answers_list = []
        print("Is the target to the {}?".format("right" if direction else "left"))
        for i in range(2 * number_of_lies + 1):
            number_of_questions += 1
            answer = tree.direction(node, direction)
            answers_list.append(answer)
            print("Answer: ", answer)
            answers += 1 if answer else -1
        number_of_lies_in_answers = min(answers_list.count(True), answers_list.count(False))
        total_received_lies += number_of_lies_in_answers
        number_of_lies = E - total_received_lies
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
    return number_of_questions



from structure import BinaryTree

E = 4

# Test
tree = BinaryTree(10, max_value=50, number_of_lies=E)
for value in tree:
    print(value)


tree.print_tree(tree.root)

tree.draw()

print("-"*50)
print("Naiive approach:")
naiive_approach_questions = naiive_approach(E)
print("End of naiive approach")
print("Number of questions asked: ", naiive_approach_questions)
print("-"*50)

print("-"*50)
print("Historical Naiive approach:")
naiive_approach_questions = historical_naiive_approach(E)
print("End of Historical naiive approach")
print("Number of questions asked: ", naiive_approach_questions)
print("-"*50)








