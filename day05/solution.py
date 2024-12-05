"""
Challenge Link: https://adventofcode.com/2024/day/5

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections
from typing import List, Set, Tuple

import read_data


def parse(data: List[List[int]]) -> Tuple[List[List[int]], List[List[int]]]:
    sep = data.index([])
    ordering, updates = data[:sep], data[sep + 1:]
    return ordering, updates


def solve_part_1(data: List[List[int]]) -> int:
    ordering, updates = parse(data)
    following_nums_rules = get_following_nums(ordering)
    valid, _ = get_valid_invalid(following_nums_rules, updates)
    return sum(update[len(update) // 2] for update in valid)


def solve_part_2(data: List[List[int]]) -> int:
    ordering, updates = parse(data)
    following_nums_rules = get_following_nums(ordering)
    _, to_fix = get_valid_invalid(following_nums_rules, updates)
    fixed = (fix(update, following_nums_rules) for update in to_fix)
    return sum(update[len(update) // 2] for update in fixed)


def get_valid_invalid(following_rules: collections.defaultdict[int, Set[int]], updates: List[List[int]]):
    valid_updates, invalid_updates = [], []
    for update in updates:
        invalid = False
        for i in range(len(update)):
            if not all(n in following_rules[update[i]] for n in update[i + 1:]):
                invalid = True
        if invalid:
            invalid_updates.append(update)
        else:
            valid_updates.append(update)
    return valid_updates, invalid_updates


def get_following_nums(ordering: List[List[int]]) -> collections.defaultdict[int, Set[int]]:
    following_rules = collections.defaultdict(set)
    for n, m in ordering:
        following_rules[n].add(m)
    return following_rules


def fix(update: List[int], following_rules: collections.defaultdict[int, Set[int]]) -> List[int]:
    fixed = []
    while update:
        n = update.pop(0)
        if all(m in following_rules[n] for m in update):
            fixed.append(n)
        else:
            update.append(n)
    return fixed


if __name__ == '__main__':
    sample = read_data.get_data_09_all_line_ints('sample.txt')
    my_input = read_data.get_data_09_all_line_ints('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
