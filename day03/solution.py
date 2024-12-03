"""
Challenge Link: https://adventofcode.com/2024/day/3

Paste sample and your input in the dedicated files and run the code to see the results.
Note: Since today's challenge uses different sample data for each part, two sample files have to be provided.
"""

import re

import read_data


def solve_part_1(data: str) -> int:
    nums = re.findall(r'mul\((\d+),(\d+)\)', data)
    return sum(int(n1) * int(n2) for n1, n2 in nums)


def solve_part_2_v1(data: str) -> int:
    data = remove_disabled(data)
    return solve_part_1(data)


def solve_part_2_v2(data: str) -> int:
    n, go = 0, True
    for expr, n1, n2 in re.findall("(don't\(\)|do\(\)|mul\((\d+),(\d+)\))", data):
        if expr == "don't()":
            go = False
        elif expr == 'do()':
            go = True
        else:
            n1, n2 = int(n1), int(n2)
            if go:
                n += int(n1) * int(n2)
    return n


def remove_disabled(data):
    one_line_data = re.sub(r'\n', '', data)
    enabled_only = re.sub(r"don't\(\).+?do\(\)|don't\(\).+$", '', one_line_data)
    return enabled_only


if __name__ == '__main__':
    sample_1 = read_data.get_data_00('sample_1.txt')
    sample_2 = read_data.get_data_00('sample_2.txt')
    my_input = read_data.get_data_00('input.txt')

    example_1 = solve_part_1(sample_1)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2_v1(sample_2)
    part_2 = solve_part_2_v1(my_input)
    print(f'Part 2:\tExample (solution v1): {example_2} | Solution: {part_2}')

    example_2 = solve_part_2_v1(sample_2)
    part_2 = solve_part_2_v1(my_input)
    print(f'Part 2:\tExample (solution v2): {example_2} | Solution: {part_2}')
