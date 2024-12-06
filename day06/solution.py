"""
Challenge Link: https://adventofcode.com/2024/day/6

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data


def solve_part_1(data: typing.List[typing.List[str]]) -> int:
    p = get_start(data)
    visited = {p}
    cur_dir = 'N'
    dir_move = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    dir_change = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
    in_area = True
    while in_area:
        x, y = dir_move[cur_dir]
        xt, yt = p[0] + x, p[1] + y
        if 0 <= xt < len(data) and 0 <= yt < len(data[0]):
            cur = data[xt][yt]
            if cur == '#':
                cur_dir = dir_change[cur_dir]
            else:
                p = xt, yt
                visited.add(p)
        else:
            in_area = False
    return len(visited)


def solve_part_2(data: typing.List[typing.List[str]]) -> int:
    s = get_start(data)

    dir_move = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    dir_change = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
    loops = 0

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != '#':
                data[i][j] = '#'
                p = s
                cur_dir = 'N'
                visited = {(p, cur_dir)}
                in_area, in_loop = True, False

                while in_area and not in_loop:
                    x, y = dir_move[cur_dir]
                    xt, yt = p[0] + x, p[1] + y
                    if 0 <= xt < len(data) and 0 <= yt < len(data[0]):
                        cur = data[xt][yt]
                        if cur == '#':
                            cur_dir = dir_change[cur_dir]
                        else:
                            p = xt, yt
                            if (p, cur_dir) in visited:
                                in_loop = True
                                loops += 1
                            visited.add((p, cur_dir))
                    else:
                        in_area = False
                data[i][j] = '.'
    return loops


def get_start(data: typing.List[typing.List[str]]) -> typing.Tuple[int, int]:
    i = 0
    while i < len(data) and '^' not in data[i]:
        i += 1
    return i, data[i].index('^')


if __name__ == '__main__':
    sample = read_data.get_data_10_all_line_strs('sample.txt')
    my_input = read_data.get_data_10_all_line_strs('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
