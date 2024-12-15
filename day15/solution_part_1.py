"""
Challenge Link: https://adventofcode.com/2024/day/15

Solution for Part 1

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data


def solve_part_1(data: typing.Tuple[typing.List[str], str]) -> int:
    area, steps = data
    area = [[c for c in row] for row in area]
    i, j = get_start(area)
    area[i][j] = '.'
    for step in steps:
        i, j = move(i, j, step, area)
    return calc_boxes_sum(area)


def get_start(area: typing.List[typing.List[str]]) -> typing.Tuple[int, int]:
    for i in range(len(area)):
        for j in range(len(area[i])):
            if '@' in area[i]:
                return i, area[i].index('@')
    return -1, -1


def move(i: int, j: int, step: str, data: typing.List[typing.List[str]]) -> typing.Tuple:
    d = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    x, y = d[step]
    if 0 <= i + x < len(data) and 0 <= j + y < len(data[i]):
        if data[i + x][j + y] == '#':
            return i, j
        if data[i + x][j + y] == '.':
            data[i][j] = '.'
            return i + x, j + y
        if data[i + x][j + y] == 'O':
            if step == '>':
                t = find_free(data, i + x, j + y, step)
                if t:
                    w, z = t
                    data[i + x][j + y], data[w][z] = data[w][z], data[i + x][j + y]
                    return i + x, j + y
            elif step == '<':
                t = find_free(data, i + x, j + y, step)
                if t:
                    w, z = t
                    data[i + x][j + y], data[w][z] = data[w][z], data[i + x][j + y]
                    return i + x, j + y
            elif step == '^':
                t = find_free(data, i + x, j + y, step)
                if t:
                    w, z = t
                    data[i + x][j + y], data[w][z] = data[w][z], data[i + x][j + y]
                    return i + x, j + y
            elif step == 'v':
                t = find_free(data, i + x, j + y, step)
                if t:
                    w, z = t
                    data[i + x][j + y], data[w][z] = data[w][z], data[i + x][j + y]
                    return i + x, j + y
    return i, j


def find_free(data: typing.List[typing.List[str]], i: int, j: int, step: str) -> typing.Tuple:
    if step == '>':
        while j < len(data[i]):
            j += 1
            if data[i][j] == '.':
                return i, j
            if data[i][j] == '#':
                return ()
    elif step == '<':
        while j > 0:
            j -= 1
            if data[i][j] == '.':
                return i, j
            if data[i][j] == '#':
                return ()
    elif step == '^':
        while i > 0:
            i -= 1
            if data[i][j] == '.':
                return i, j
            if data[i][j] == '#':
                return ()
    elif step == 'v':
        while i < len(data):
            i += 1
            if data[i][j] == '.':
                return i, j
            if data[i][j] == '#':
                return ()
    return ()


def calc_boxes_sum(area: typing.List[typing.List[str]]) -> int:
    return sum(100 * i + j for i in range(len(area)) for j in range(len(area[i])) if area[i][j] in {'O', '['})


def parse_data(data: typing.List[str]) -> typing.Tuple[typing.List[str], str]:
    blank = data.index('')
    data = (data[:blank], ''.join(data[blank + 1:]))
    return data


if __name__ == '__main__':
    sample_small = parse_data(read_data.get_data_02_str_list('sample_small.txt'))
    sample_large = parse_data(read_data.get_data_02_str_list('sample_large.txt'))
    my_input = parse_data(read_data.get_data_02_str_list('input.txt'))

    example_small = solve_part_1(sample_small)
    example_large = solve_part_1(sample_large)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\n\tExample:\n\t\tSmall sample: {example_small}\n\t\tLarge sample: {example_large}\n\t'
          f'Solution: {part_1}')

    print(f'\nPart 2:\tSolution to part 2 can be found in solution_part_2.py')
