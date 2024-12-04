"""
Challenge Link: https://adventofcode.com/2024/day/4

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data


def solve_part_1(data: typing.List[str]) -> int:
    cnt = count_horizontal(data) + count_horizontal(transpose(data)) + count_diagonal(data)
    return cnt


def count_horizontal(data: typing.List[str]) -> int:
    return sum(row.count('XMAS') + row.count('SAMX') for row in data)


def transpose(data: typing.List[str]) -> typing.List[str]:
    t = [''.join([data[j][i] for j in range(len(data))]) for i in range(len(data[0]))]
    return t


def count_diagonal(data: typing.List[str]) -> int:
    found = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i + 3 < len(data) and j + 3 < len(data[i]) and \
                    f'{data[i][j]}{data[i + 1][j + 1]}{data[i + 2][j + 2]}{data[i + 3][j + 3]}' in {'XMAS', 'SAMX'}:
                found.add(tuple(sorted([(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)])))
            if i + 3 < len(data) and j - 3 >= 0 and \
                    f'{data[i][j]}{data[i + 1][j - 1]}{data[i + 2][j - 2]}{data[i + 3][j - 3]}' in {'XMAS', 'SAMX'}:
                found.add(tuple(sorted([(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)])))
            if i - 3 >= 0 and j + 3 < len(data[i]) and \
                    f'{data[i][j]}{data[i - 1][j + 1]}{data[i - 2][j + 2]}{data[i - 3][j + 3]}' in {'XMAS', 'SAMX'}:
                found.add(tuple(sorted([(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)])))
    return len(found)


def solve_part_2(data: typing.List[str]) -> int:
    cnt = 0
    for i in range(len(data) - 2):
        for j in range(len(data[i]) - 2):
            if data[i][j] == 'M' and data[i + 1][j + 1] == 'A' and data[i + 2][j + 2] == 'S':
                if (data[i + 2][j] == 'M' and data[i][j + 2] == 'S') or (
                        data[i + 2][j] == 'S' and data[i][j + 2] == 'M'):
                    cnt += 1
            elif data[i][j] == 'S' and data[i + 1][j + 1] == 'A' and data[i + 2][j + 2] == 'M':
                if (data[i + 2][j] == 'M' and data[i][j + 2] == 'S') or (
                        data[i + 2][j] == 'S' and data[i][j + 2] == 'M'):
                    cnt += 1
    return cnt


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
