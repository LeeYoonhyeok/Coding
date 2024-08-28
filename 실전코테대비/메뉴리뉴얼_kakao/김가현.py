from itertools import combinations
from collections import Counter


def solution(orders, course):
    popular_combinations = []

    for combination_size in course:
        possible_combinations = []

        for order in orders:
            for combination in combinations(order, combination_size):
                sorted_combination = ''.join(sorted(combination))
                possible_combinations.append(sorted_combination)

        combination_frequencies = Counter(possible_combinations).most_common()

        if combination_frequencies:
            max_frequency = combination_frequencies[0][1]
            popular_combinations.extend([
                combination for combination, frequency in combination_frequencies
                if frequency > 1 and frequency == max_frequency
            ])

    return sorted(popular_combinations)