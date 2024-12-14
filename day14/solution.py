"""
Challenge Link: https://adventofcode.com/2024/day/14

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import functools
import typing

import read_data


def solve_part_1(data: typing.List[typing.List[int]], lx: int, ly: int) -> int:
    seconds = 100
    quadrant_cnts = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    for x, y, vx, vy in data:
        x, y = move(x, y, vx, vy, lx, ly, seconds)
        q = get_quadrant(x, y, lx, ly)
        if q != ():
            quadrant_cnts[q] += 1
    return functools.reduce(lambda a, b: a * b, quadrant_cnts.values(), 1)


def solve_part_2(data: typing.List[typing.List[int]], lx: int, ly: int, picture: str) -> None:
    with open(f'{picture}.txt', 'a') as f:
        for t in range(10000):
            f.write(f'\n{t}\n')
            points = [move(x, y, vx, vy, lx, ly, t) for x, y, vx, vy in data]
            write(lx, ly, points, f)


def move(x: int, y: int, vx: int, vy: int, len_x: int, len_y: int, time: int) -> typing.Tuple:
    x = (x + vx * time) % len_x
    y = (y + vy * time) % len_y
    return x, y


def get_quadrant(x: int, y: int, len_x: int, len_y: int) -> typing.Tuple:
    if x == len_x // 2 or y == len_y // 2:
        return ()
    qx = 0 if x < len_x // 2 else 1
    qy = 0 if y < len_y // 2 else 1
    return qx, qy


def write(lx: int, ly: int, points: typing.List[typing.Tuple[int, int]], file: typing.IO) -> None:
    for row in get_area_state(lx, ly, points):
        joined = ''.join(row)
        file.write(joined)
        file.write('\n')


def get_area_state(lx: int, ly: int, points: typing.List[typing.Tuple[int, int]]) -> typing.List[typing.List[str]]:
    area = [['.' for _ in range(lx)] for _ in range(ly)]
    for x, y in points:
        area[y][x] = '#'
    return area


if __name__ == '__main__':
    sample = read_data.get_data_09_all_line_ints('sample.txt')
    my_input = read_data.get_data_09_all_line_ints('input.txt')

    example_1 = solve_part_1(sample, 7, 11)
    part_1 = solve_part_1(my_input, 101, 103)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    solve_part_2(my_input, 101, 103, 'output')
    print(f'Part 2:\tThe result is written in the output file. Christmas tree should be found there.'
          f'\n\t\tHint: look for consecutive "#" characters to find the result faster.')
