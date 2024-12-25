"""
Challenge Link: https://adventofcode.com/2024/day/24

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import re
import typing

import read_data


def solve_part_1(data: typing.List[typing.List[str]]) -> int:
    s = data.index([])
    d = {k: int(v) for k, v in data[:s]}

    operations = data[s + 1:]
    while operations:
        for i, (k1, op, k2, v) in enumerate(operations):
            if k1 not in d or k2 not in d:
                continue
            v1, v2 = d[k1], d[k2]
            if op == 'AND':
                d[v] = v1 and v2
            elif op == 'OR':
                d[v] = v1 or v2
            elif op == 'XOR':
                d[v] = v1 ^ v2
            operations.pop(i)
    return sum_z_wires(d)


def sum_z_wires(d: typing.Dict[str, int]) -> int:
    binary = ''.join(str(v) for k, v in sorted(d.items(), reverse=True) if k[0] == 'z')
    return int(binary, 2)


def parse_data(data: str) -> typing.List[typing.List[str]]:
    return [re.findall(r'\w+', line) for line in data.split('\n')]


if __name__ == '__main__':
    sample = parse_data(read_data.get_data_00('sample.txt'))
    my_input = parse_data(read_data.get_data_00('input.txt'))

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')
    print(f'Part 2:\tPartially manual solution. Approach description and helper functions to come.')
