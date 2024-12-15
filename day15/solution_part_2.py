"""
Challenge Link: https://adventofcode.com/2024/day/15

Solution for Part 2

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data
from day15.solution_part_1 import get_start, parse_data, calc_boxes_sum, find_free


def solve_part_2(data: typing.Tuple[typing.List[str], str]) -> int:
    area, steps = data
    area = [[c for c in row] for row in area]
    i, j = get_start(area)
    area[i][j] = '.'
    area = double_area(area)
    j *= 2
    area[i][j] = '@'
    for step in steps:
        area[i][j] = '.'
        i, j = move_2(i, j, step, area)
        area[i][j] = '@'
    return calc_boxes_sum(area)


def move_2(i: int, j: int, step: str, data: typing.List[typing.List[str]]) -> typing.Tuple:
    d = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    x, y = d[step]
    if 0 <= i + x < len(data) and 0 <= j + y < len(data[i]):
        if data[i + x][j + y] == '#':
            return i, j
        if data[i + x][j + y] == '.':
            data[i][j] = '.'
            return i + x, j + y
        if data[i + x][j + y] in {'[', ']'}:
            if step == '>':
                t = find_free(data, i + x, j + y, step)
                if t:
                    w, z = t
                    data[i + x][j + y + 1:z + 1] = data[i + x][j + y:z]
                    data[i + x][j + y] = '.'
                    return i + x, j + y
            elif step == '<':
                t = find_free(data, i + x, j + y, step)
                if t:
                    w, z = t
                    data[i][j] = '.'
                    data[i + x][z:j + y] = data[i + x][z + 1:j + y + 1]
                    return i + x, j + y
            elif step in {'^', 'v'}:
                to_move = get_all_to_move(data, i + x, j + y, step)
                if can_move_multiple(data, to_move, step):
                    move_multiple(data, to_move, step)
                    return i + x, j + y
    return i, j


def can_move_multiple(data: typing.List[typing.List[str]], to_move: typing.Set[typing.Tuple[int, int]],
                      step: str) -> bool:
    copied = [[cell for cell in row] for row in data]
    v = 1 if step == 'v' else -1
    for i, j in to_move:
        copied[i][j] = '.'
    for i, j in to_move:
        if not (0 <= i < len(data) and copied[i + v][j] == '.'):
            return False
    return True


def move_multiple(data: typing.List[typing.List[str]], to_move: typing.Set[typing.Tuple[int, int]], step: str) -> None:
    v = 1 if step == 'v' else -1
    left = {(i, j) for i, j in to_move if data[i][j] == '['}
    right = {(i, j) for i, j in to_move if data[i][j] == ']'}
    for i, j in to_move:
        data[i][j] = '.'
    for i, j in left:
        data[i + v][j] = '['
    for i, j in right:
        data[i + v][j] = ']'


def get_all_to_move(data: typing.List[typing.List[str]], i: int, j: int, step: str) -> typing.Set[
    typing.Tuple[int, int]]:
    to_move = get_pair(data, i, j)
    togo = {p for p in to_move}
    while togo:
        x, y = togo.pop()
        next_pair = get_next(data, x, y, step)
        to_move |= next_pair
        togo |= next_pair
    return to_move


def get_pair(data: typing.List[typing.List[str]], i: int, j: int) -> typing.Set[typing.Tuple[int, int]]:
    if data[i][j] == '[':
        return {(i, j), (i, j + 1)}
    if data[i][j] == ']':
        return {(i, j), (i, j - 1)}
    return set()


def get_lower(data: typing.List[typing.List[str]], i: int, j: int) -> typing.Set[typing.Tuple[int, int]]:
    if data[i + 1][j] in {'[', ']'}:
        return get_pair(data, i + 1, j)
    return set()


def get_upper(data: typing.List[typing.List[str]], i: int, j: int) -> typing.Set[typing.Tuple[int, int]]:
    if data[i - 1][j] in {'[', ']'}:
        return get_pair(data, i - 1, j)
    return set()


def get_next(data: typing.List[typing.List[str]], i: int, j: int, step: str) -> typing.Set[typing.Tuple[int, int]]:
    if step == 'v':
        return get_lower(data, i, j)
    if step == '^':
        return get_upper(data, i, j)
    return set()


def double_area(area: typing.List[typing.List[str]]) -> typing.List[typing.List[str]]:
    doubled = []
    for i in range(len(area)):
        row = []
        for j in range(len(area[i])):
            if area[i][j] == 'O':
                row.extend(['[', ']'])
            else:
                row.extend([area[i][j], area[i][j]])
        doubled.append(row)
    return doubled


if __name__ == '__main__':
    sample = parse_data(read_data.get_data_02_str_list('sample_large.txt'))
    my_input = parse_data(read_data.get_data_02_str_list('input.txt'))

    print(f'Part 1:\tSolution to part 1 can be found in solution_part_1.py\n')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
