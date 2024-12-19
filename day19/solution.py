"""
Challenge Link: https://adventofcode.com/2024/day/19

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data


def solve(data: typing.List[str]) -> typing.Tuple[int, int]:
    sp = data.index('')
    patterns = set(data[0].split(', '))
    towels = data[sp + 1:]
    arrangements = [count_arrangements(towel, patterns, {}) for towel in towels]
    return sum(1 for a in arrangements if a), sum(arrangements)


def count_arrangements(towel: str, patterns: typing.Set[str], memo: typing.Dict[str, int]):
    if towel in memo:
        return memo[towel]
    if not towel:
        return 1
    memo[towel] = sum(
        count_arrangements(towel[len(p):], patterns, memo) if towel.startswith(p) else 0 for p in patterns)
    return memo[towel]


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example = solve(sample)
    part = solve(my_input)
    print(f'Part 1:\tExample: {example[0]} | Solution: {part[0]}')
    print(f'Part 2:\tExample: {example[1]} | Solution: {part[1]}')
