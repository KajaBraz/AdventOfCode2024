"""
Challenge Link: https://adventofcode.com/2024/day/8

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections
import typing

import read_data


def solve_part_1(data: typing.List[str]) -> int:
    antennas = get_antennas(data)
    antinodes = set()

    for antenna, points in antennas.items():
        for i, j in sorted(points):
            for x, y in sorted(points):
                if (x, y) != (i, j):
                    horizontal_freq, vertical_freq = x - i, y - j
                    for a, b in [(x + horizontal_freq, y + vertical_freq), (i - horizontal_freq, j - vertical_freq)]:
                        if 0 <= a < len(data) and 0 <= b < len(data[0]):
                            antinodes.add((a, b))
    return len(antinodes)


def solve_part_2(data: typing.List[str]) -> int:
    antennas = get_antennas(data)
    antinodes = set()

    for antenna, points in antennas.items():
        for i, j in sorted(points):
            for x, y in sorted(points):
                if (x, y) != (i, j):
                    horizontal_freq, vertical_freq = x - i, y - j
                    for a, b, operation in [(x, y, lambda e1, e2: e1 + e2), (i, j, lambda e1, e2: e1 - e2)]:
                        while 0 <= a < len(data) and 0 <= b < len(data[0]):
                            antinodes.add((a, b))
                            a, b = operation(a, horizontal_freq), operation(b, vertical_freq)
    return len(antinodes)


def get_antennas(data: typing.List[str]) -> collections.defaultdict[str, typing.Set[typing.Tuple[int, int]]]:
    antennas = collections.defaultdict(set)
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != '.':
                antennas[cell].add((i, j))
    return antennas


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
