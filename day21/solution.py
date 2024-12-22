"""
Challenge Link: https://adventofcode.com/2024/day/21

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import itertools
import math
import typing

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


def solve_part_1(data) -> int:
    return solve(data, 2)


def solve_part_2(data: typing.List[str]) -> int:
    return solve(data, 25)


def solve(data, chain_len):
    result = 0
    for code in data:
        d = int(code[:-1])
        candidates = reach_nums(code)
        temp = []
        for candidate in candidates:
            temp.append(solve_rec(f'A{candidate}', chain_len, {}))
        seq_len = min(temp)
        result += (d * seq_len)
    return result


def solve_rec(p: str, level: int, memo: typing.Dict[typing.Tuple[str, int], int]) -> int:
    t = (p, level)
    if t in memo:
        return memo[t]
    if level == 0:
        return len(p) - 1
    result = 0
    for i in range(1, len(p)):
        r = math.inf
        pp = [''.join(t) for t in get_from_to_arrow_path(p[i - 1], p[i])]
        for ppp in pp:
            r = min(r, solve_rec(f'A{ppp}A', level - 1, memo))
        result += r
    memo[t] = result
    return memo[t]


def get_from_to_num_path(source: str, target: str) -> typing.List[typing.Tuple]:
    x, y = NUMS[source]
    i, j = NUMS[target]
    horizontal = y - j
    vertical = x - i
    path = get_dir_arrows(True, horizontal) + get_dir_arrows(False, vertical)
    paths = get_variants(path)
    return [path for path in paths if is_legal(path, (x, y), (3, 0))]


def get_from_to_arrow_path(source: str, target: str) -> typing.List[typing.Tuple]:
    x, y = ARROWS[source]
    i, j = ARROWS[target]
    horizontal = y - j
    vertical = x - i
    path = get_dir_arrows(True, horizontal) + get_dir_arrows(False, vertical)
    paths = get_variants(path)
    paths = [path for path in paths if is_legal(path, (x, y), (0, 0))]
    return paths


def get_variants(path: str) -> itertools.permutations:
    return itertools.permutations(path)


def is_legal(possible_path: typing.Tuple, cur_pos: typing.Tuple[int, int], illegal_pos: typing.Tuple[int, int]) -> bool:
    displacement = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}
    for c in possible_path:
        m, n = displacement[c]
        cur_pos = cur_pos[0] + m, cur_pos[1] + n
        if cur_pos == illegal_pos:
            return False
    return True


def get_dir_arrows(is_horizontal: bool, diff: int) -> str:
    if is_horizontal:
        arrow = '>' if diff <= 0 else '<'
        return arrow * abs(diff)
    arrow = 'v' if diff <= 0 else '^'
    return arrow * abs(diff)


def reach_nums(target_code: str) -> typing.List[str]:
    current_button = 'A'
    result = []
    for button in target_code:
        result.append(set(''.join(p) for p in get_from_to_num_path(current_button, button)))
        current_button = button
    final = result[0]
    for i in range(1, len(result)):
        final = [f'{f}A{p}' for f in final for p in result[i]]
    return [f'{p}A' for p in final]


def intermediate_move(target_path: str) -> typing.List[str]:
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


def solve_part_1_alternative(data: typing.List[str]) -> int:
    r = 0
    for code in data:
        d = int(code[:-1])
        p1 = reach_nums(code)
        p2 = []
        for p in p1:
            p2.extend(intermediate_move(p))
        p3 = []
        for p in p2:
            p3.extend(intermediate_move(p))
        r = r + d * len(min(p3, key=len))
    return r


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    # Alternative solution for part 1
    # example_1 = solve_part_1_alternative(sample)
    # part_1 = solve_part_1_alternative(my_input)
    # print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
