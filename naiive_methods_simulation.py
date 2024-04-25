import random
import csv

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



import numpy as np

def experiment(size, total_number_of_lies):
    number_of_lies = total_number_of_lies
    number_of_seen_lies = 0
    num_asked_questions = 0
    min_num = 1
    max_num = size

    # Random selection using NumPy
    target = np.random.choice(size)
    lie_places = np.random.choice(size.bit_length() * (number_of_lies * 2 + 1), number_of_lies, replace=False)



    while max_num - min_num > 1:
        guess = (max_num + min_num) // 2
        is_it_right = np.random.choice([True, False])  # Randomly determine direction

        if guess <= target:
            min_num = guess
        else:
            max_num = guess

        i = 0
        new_lie_detected = False
        while i < 2 * number_of_lies + 1:
            if num_asked_questions in lie_places:
                number_of_seen_lies += 1
                new_lie_detected = True
            i += 1
            num_asked_questions += 1

        number_of_lies = total_number_of_lies - number_of_seen_lies
        if new_lie_detected:
            # Update lie_places range for subsequent rounds
            lie_places = np.random.choice(np.arange(num_asked_questions, num_asked_questions + (max_num - min_num).bit_length() * ((total_number_of_lies - number_of_seen_lies) * 2 + 1)), total_number_of_lies - number_of_seen_lies, replace=False)

    if number_of_seen_lies < total_number_of_lies:
        num_asked_questions += (total_number_of_lies - number_of_seen_lies) * 2 + 1

    # print("Number of questions asked: ", num_asked_questions)
    return num_asked_questions


# Prepare CSV file
with open('experiment_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Experiment Number", "Size", "Number of Lies", "Mean Questions", "Std Deviation"])


    # Sample usage
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    lie_fraction = [0, 0.1, 0.2, 0.3, 0.4, 0.5]



    experiment_number = 0
    max_itr_number = 1000
    for size in sizes:
        for fraction in lie_fraction:
            experiment_number += 1
            experimentResults = []
            print("-" * 50)
            print("Experiment number: ", experiment_number)
            print("Number of lies: ", int(size * fraction))
            print("Size: ", size)
            for i in range(max_itr_number):
                # print("Size: ", size, "Fraction: ", fraction)
                experimentResults.append(experiment(size, int(size * fraction)))
            print("Results: ", experimentResults)
            print("mean and std: ", np.mean(experimentResults), np.std(experimentResults))
            writer.writerow([experiment_number, size, int(size * fraction), np.mean(experimentResults), np.std(experimentResults)])
            print("-" * 50)

# experiment(10000, 50)

# if last_direction_was_right:
#     if guess+1 <= target:
#         max_num = guess+1
#     else:
#         min_num = guess
#     print("Target found!", max_num)
# else:
#     print("Target found!", min_num)



