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


def solve_part_2(data: typing.List[typing.List[str]], verbose: bool, inspection_level: int = 3) -> typing.List[str]:
    s = data.index([])

    operations = {v: (k1, op, k2) for k1, op, k2, v in data[s + 1:]}
    operations_pattern_level_3 = re.compile(r'[\w\(]+ AND [\w\)]+ OR [\w\(]+ AND [\w\)]+ XOR [\w\(]+ XOR [\w\)]+')

    potential_needing_swaps = []

    for i in range(100):
        cur_z = f'z{str(i).zfill(2)}'
        if cur_z in operations:
            operations_chain = find_operations_chain(operations, cur_z, inspection_level)
            if inspection_level == 3:
                matching = re.match(operations_pattern_level_3, operations_chain)
                if not matching:
                    potential_needing_swaps.append(cur_z)
            if verbose:
                print(f'{cur_z} -> {operations_chain}')
    return potential_needing_swaps


def find_operations_chain(operations_dict: typing.Dict[str, typing.Tuple[str, str, str]], cur_key: str,
                          level: int) -> str:
    if level == 0:
        return cur_key
    a, operation, b = operations_dict[cur_key]
    if a[0] not in {'x', 'y'}:
        a = find_operations_chain(operations_dict, a, level - 1)
    if b[0] not in {'x', 'y'}:
        b = find_operations_chain(operations_dict, b, level - 1)
    a, b = (a, b) if a < b else (b, a)
    return f'({a} {operation} {b})'


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
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}\n')

    print(f'Part 2:\tPartially manual solution. '
          f'Verify the gates listed below by investigating them in your input data. '
          f'Try to swap unmatched elements in their operation chain to see if this will lead you to fixing the system. '
          f'Note that swapping one element can change the other potential incorrect gates (the below output). '
          f'If you want to see the detailed operation chain for each z-gate, '
          f'run the function with the verbose param set to True. Otherwise change it to False.\n')
    part_2 = solve_part_2(my_input, True, 3)
    print(f'\nInvestigate the following gates: {part_2}')
