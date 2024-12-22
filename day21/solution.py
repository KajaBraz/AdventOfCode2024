"""
Challenge Link: https://adventofcode.com/2024/day/21

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import itertools
import re

import read_data

NUMS = {'A': (3, 2),
        '0': (3, 1),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2)}

ARROWS = {'A': (0, 2),
          '^': (0, 1),
          '<': (1, 0),
          'v': (1, 1),
          '>': (1, 2)}


def get_from_to_num_path(source, target):
    x, y = NUMS[source]
    i, j = NUMS[target]
    horizontal = y - j
    vertical = x - i
    if x == 3:
        path = get_dir_arrows(False, vertical) + get_dir_arrows(True, horizontal)
    else:
        path = get_dir_arrows(True, horizontal) + get_dir_arrows(False, vertical)
    paths = get_variants(path)
    return [path for path in paths if is_legal(path, (x, y), (3, 0))]


def get_from_to_arrow_path(source, target):
    x, y = ARROWS[source]
    i, j = ARROWS[target]
    horizontal = y - j
    vertical = x - i
    if x == 0:
        path = get_dir_arrows(False, vertical) + get_dir_arrows(True, horizontal)
    else:
        path = get_dir_arrows(True, horizontal) + get_dir_arrows(False, vertical)
    paths = get_variants(path)
    paths = [path for path in paths if is_legal(path, (x, y), (0, 0))]
    return paths


def get_variants(path):
    p = itertools.permutations(path)
    return p


def is_legal(possible_path, cur_pos, illegal_pos):
    m, n = 0, 0
    for c in possible_path:
        if c == 'v':
            m, n = 1, 0
        elif c == '^':
            m, n = -1, 0
        elif c == '<':
            m, n = 0, -1
        elif c == '>':
            m, n = 0, 1
        cur_pos = cur_pos[0] + m, cur_pos[1] + n
        if cur_pos == illegal_pos:
            return False
    return True


def solve(code):
    if len(code) < 2:
        return set()


def get_dir_arrows(is_horizontal, diff):
    if is_horizontal:
        arrow = '>' if diff <= 0 else '<'
        return arrow * abs(diff)
    arrow = 'v' if diff <= 0 else '^'
    return arrow * abs(diff)


def reach_nums(target_code):
    current_button = 'A'
    result = []
    for button in target_code:
        result.append(set(''.join(p) for p in get_from_to_num_path(current_button, button)))
        current_button = button
    final = result[0]
    for i in range(1, len(result)):
        final = [f'{f}A{p}' for f in final for p in result[i]]
    return [f'{p}A' for p in final]


def intermediate_move(target_path):
    current_button = 'A'
    result = []
    for button in target_path:
        t = [''.join(p) for p in get_from_to_arrow_path(current_button, button)]
        t = set(t)
        result.append(t)
        current_button = button
    result = [r for r in result if r]
    final = result[0]
    for i in range(1, len(result)):
        final = [f'{f}A{p}' for f in final for p in result[i]]
    return [f'{p}A' for p in final]


def solve_part_1(data) -> int:
    r = 0
    for code in data:
        d = re.findall(r'\d+', code)[0]
        p1 = reach_nums(code)
        p2 = []
        for p in p1:
            p2.extend(intermediate_move(p))
        p3 = []
        for p in p2:
            p3.extend(intermediate_move(p))
        r = r + int(d) * len(min(p3, key=len))
    return r


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')
