"""
Challenge Link: https://adventofcode.com/2024/day/7

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data


def solve_part_1(data: typing.List[typing.List[int]]) -> int:
    res = 0
    for operation in data:
        r, nums = operation[0], operation[1:]
        if solve(r, nums[0], nums[1:]):
            res += r
    return res


def solve_part_2(data: typing.List[typing.List[int]]) -> int:
    res = 0
    for operation in data:
        r, nums = operation[0], operation[1:]
        if solve(r, nums[0], nums[1:], True):
            res += r
    return res


def solve(target: int, temp_res: int, nums: typing.List[int], concatenate: bool = False):
    if not nums:
        return temp_res == target

    m = solve(target, temp_res * nums[0], nums[1:], concatenate)
    p = solve(target, temp_res + nums[0], nums[1:], concatenate)

    if not concatenate:
        return m or p

    c = solve(target, int(f'{temp_res}{nums[0]}'), nums[1:], concatenate)
    return m or p or c


if __name__ == '__main__':
    sample = read_data.get_data_09_all_line_ints('sample.txt')
    my_input = read_data.get_data_09_all_line_ints('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
