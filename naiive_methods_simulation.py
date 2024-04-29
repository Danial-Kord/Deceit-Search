import random
import csv


import numpy as np

def experiment(size, total_number_of_lies, probability = 0.5, arbitrary=False):
    number_of_lies = total_number_of_lies
    number_of_seen_lies = 0
    num_asked_questions = 0
    min_num = 1
    max_num = size

    # Random selection using NumPy
    target = np.random.choice(size)
    # lie_places = np.random.choice(size.bit_length() * (number_of_lies * 2 + 1), number_of_lies, replace=False)



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
            if number_of_lies != 0 and random.random() < probability:
                number_of_seen_lies += 1
                new_lie_detected = True
            i += 1
            num_asked_questions += 1

        number_of_lies = total_number_of_lies - number_of_seen_lies
        # if new_lie_detected:
        #     # Update lie_places range for subsequent rounds
        #     lie_places = np.random.choice(np.arange(num_asked_questions, num_asked_questions + (max_num - min_num).bit_length() * ((total_number_of_lies - number_of_seen_lies) * 2 + 1)), total_number_of_lies - number_of_seen_lies, replace=False)

    if number_of_seen_lies < total_number_of_lies:
        num_asked_questions += (total_number_of_lies - number_of_seen_lies) * 2 + 1

    # print("Number of questions asked: ", num_asked_questions)
    return num_asked_questions


def continues_case(epsilon, probability = 0.5):
    total_number_of_lies = int((1 / epsilon) * probability)
    number_of_lies = total_number_of_lies

    number_of_seen_lies = 0
    num_asked_questions = 0


    # Random float between 0 and 1
    target = random.random()

    # lie_places = np.random.choice(size.bit_length() * (number_of_lies * 2 + 1), number_of_lies, replace=False)

    max_num = 1.0
    min_num = 0.0
    # print("Target: ", target)
    while max_num - min_num > epsilon:

        guess = (max_num + min_num) / 2.0

        is_it_right = np.random.choice([True, False])  # Randomly determine direction

        if guess <= target:
            min_num = guess
        else:
            max_num = guess

        i = 0
        new_lie_detected = False
        while i < 2 * number_of_lies + 1:
            if number_of_lies != 0 and random.random() < probability:
                number_of_seen_lies += 1
                new_lie_detected = True
            i += 1
            num_asked_questions += 1

        number_of_lies = total_number_of_lies - number_of_seen_lies
        # if new_lie_detected:
        #     # Update lie_places range for subsequent rounds
        #     lie_places = np.random.choice(np.arange(num_asked_questions, num_asked_questions + (max_num - min_num).bit_length() * ((total_number_of_lies - number_of_seen_lies) * 2 + 1)), total_number_of_lies - number_of_seen_lies, replace=False)

    if number_of_seen_lies < total_number_of_lies:
        num_asked_questions += (total_number_of_lies - number_of_seen_lies) * 2 + 1

    # print("Number of questions asked: ", num_asked_questions)
    # print("Target: ", target)
    # print("max_num: ", max_num)
    # print("min_num: ", min_num)
    # print(index)
    return num_asked_questions



def simulate_naiive_historical():
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
                    experimentResults.append(experiment(size, int(size * fraction), probability=fraction))
                print("Results: ", experimentResults)
                print("mean and std: ", np.mean(experimentResults), np.std(experimentResults))
                writer.writerow([experiment_number, size, int(size * fraction), np.mean(experimentResults),
                                 np.std(experimentResults)])
                print("-" * 50)

def simulate_naiive_historical_continues_case():
    # Prepare CSV file
    with open('cs_case_experiment_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment Number", "Epsilon", "Number of Lies", "Mean Questions", "Std Deviation"])

        # Sample usage
        epsilons = [0.01,0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001]
        lie_fraction = [0, 0.1, 0.2, 0.3, 0.4, 0.5]

        experiment_number = 0
        max_itr_number = 1000
        for epsilon in epsilons:
            for fraction in lie_fraction:
                experiment_number += 1
                experimentResults = []
                print("-" * 50)
                print("Experiment number: ", experiment_number)
                print("Number of lies: ", int((1.0/epsilon) * fraction))
                print("Epsilon: ", epsilon)
                for i in range(max_itr_number):
                    # print("Size: ", size, "Fraction: ", fraction)
                    experimentResults.append(continues_case(epsilon, probability=fraction))
                print("Results: ", experimentResults)
                print("mean and std: ", np.mean(experimentResults), np.std(experimentResults))
                writer.writerow([experiment_number, epsilon, int((1.0/epsilon) * fraction), np.mean(experimentResults),
                                 np.std(experimentResults)])
                print("-" * 50)


simulate_naiive_historical_continues_case()

# experiment(10000, 50)

# if last_direction_was_right:
#     if guess+1 <= target:
#         max_num = guess+1
#     else:
#         min_num = guess
#     print("Target found!", max_num)
# else:
#     print("Target found!", min_num)



