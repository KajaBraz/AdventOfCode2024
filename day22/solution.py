"""
Challenge Link: https://adventofcode.com/2024/day/22

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections
import typing

import read_data


def solve_part_1(data: typing.List[int]) -> int:
    return sum(calculate_secret(n, 2000) for n in data)


def solve_part_2(data: typing.List[int]) -> int:
    sequence_totals = collections.defaultdict(int)

    for n in data:
        generated_secrets = []

        for _ in range(2000):
            n = calculate_secret(n)
            generated_secrets.append(n)

        prices = [n % 10 for n in generated_secrets]
        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

        current_sequences = set()

        for i in range(len(changes) - 3):
            sequence = tuple(changes[i:i + 4])
            if sequence not in current_sequences:
                price = prices[i + 4]
                sequence_totals[sequence] += price
                current_sequences.add(sequence)

    return get_best_total_price(sequence_totals)


def mix(n: int, v: int) -> int:
    return v ^ n


def prune(n: int) -> int:
    return n % 16777216


def calculate_secret(n: int, iteration: int = 1) -> int:
    for _ in range(iteration):
        v = n * 64
        n = prune(mix(n, v))
        v = n // 32
        n = prune(mix(n, v))
        v = n * 2048
        n = prune(mix(n, v))
    return n


def get_best_total_price(totals_dict: collections.defaultdict) -> int:
    return max(totals_dict.values())


if __name__ == '__main__':
    sample = read_data.get_data_01_int_list('sample.txt')
    my_input = read_data.get_data_01_int_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
