"""
Challenge Link: https://adventofcode.com/2024/day/25

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data


def solve_part_1(data: typing.List[str]) -> int:
    transposed = parse(data)
    locks = [get_lock_pins(block) for block in transposed if block[0][0] == '#']
    pins = [get_lock_pins(block) for block in transposed if block[0][0] == '.']
    return cnt_matching(locks, pins, len(transposed[0]))


def get_lock_pins(block: typing.List[str]) -> typing.List[int]:
    tr = [[block[j][i] for j in range(len(block))] for i in range(len(block[0]))]
    cl = [row.count('#') - 1 for row in tr]
    return cl


def cnt_matching(locks: typing.List[typing.List[int]], pins: typing.List[typing.List[int]], block_height: int) -> int:
    n_cl = len(locks[0])
    return sum(all(lock[i] + pin[i] < block_height - 1 for i in range(n_cl)) for pin in pins for lock in locks)


def parse(data: typing.List[str]) -> typing.List[typing.List[str]]:
    sp = data.index('')
    return [data[i:i + sp] for i in range(0, len(data), sp + 1)]


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')
