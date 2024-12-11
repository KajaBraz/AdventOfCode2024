"""
Challenge Link: https://adventofcode.com/2024/day/11

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections
import typing

import read_data


def solve(data: typing.List[int], k: int) -> int:
    cnts = collections.Counter(data)
    for _ in range(k):
        cnts = transform_stones(cnts)
    return sum(cnts.values())


def transform_stones(cnts: collections.Counter[int]) -> collections.Counter[int]:
    transformed = collections.Counter()
    for stone, cnt in cnts.items():
        update_stone(stone, transformed, cnt)
    return transformed


def update_stone(stone: int, d: collections.Counter[int], cnt: int) -> None:
    if stone == 0:
        d[1] += cnt
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        d[int(a)] += cnt
        d[int(b)] += cnt
    else:
        d[stone * 2024] += cnt


if __name__ == '__main__':
    sample = read_data.get_data_01_int_list('sample.txt')
    my_input = read_data.get_data_01_int_list('input.txt')

    example_1 = solve(sample, 25)
    part_1 = solve(my_input, 25)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve(sample, 75)
    part_2 = solve(my_input, 75)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
