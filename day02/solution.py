"""
Challenge Link: https://adventofcode.com/2024/day/2

Paste sample and your input in the dedicated files and run the code to see the results.
"""

from typing import List

import read_data


def solve_part_1(data: List[List[int]]) -> int:
    return sum(is_safe(row) for row in data)


def solve_part_2(data: List[List[int]]) -> int:
    safe = 0
    for row in data:
        incr, decr = is_increasing(row), is_decreasing(row)
        if any((incr, decr)):
            safe += 1
        else:
            for i in range(len(row)):
                if drop_check(row, i):
                    safe += 1
                    break
    return safe


def is_increasing(row: List[int]) -> bool:
    for i in range(len(row) - 1):
        if not (1 <= row[i] - row[i + 1] <= 3):
            return False
    return True


def is_decreasing(row: List[int]) -> bool:
    for i in range(len(row) - 1):
        if not (1 <= row[i + 1] - row[i] <= 3):
            return False
    return True


def is_safe(row: List[int]) -> bool:
    return is_increasing(row) or is_decreasing(row)


def drop_check(row: List[int], i: int) -> bool:
    dropped = row[:i] + row[i + 1:]
    return is_safe(dropped)


if __name__ == '__main__':
    sample = read_data.get_data_03_two_dim_int_list('sample.txt')
    my_input = read_data.get_data_03_two_dim_int_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
