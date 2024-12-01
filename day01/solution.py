"""
Challenge Link: https://adventofcode.com/2024/day/1

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections

import read_data


def solve_part_1(data) -> int:
    l1 = sorted(n for n, _ in data)
    l2 = sorted(n for _, n in data)
    return sum(max(l1[i], l2[i]) - min(l2[i], l1[i]) for i in range(len(data)))


def solve_part_2(data) -> int:
    l1 = {n for n, _ in data}
    l2 = (n for _, n in data)
    l2 = collections.Counter(l2)
    return sum(n * l2[n] for n in l1)


if __name__ == '__main__':
    sample = read_data.get_data_03_two_dim_int_list('sample.txt')
    my_input = read_data.get_data_03_two_dim_int_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
