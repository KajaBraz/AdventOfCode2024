"""
Challenge Link: https://adventofcode.com/2024/day/9

Paste sample and your input in the dedicated files and run the code to see the results.
"""

from itertools import chain
from typing import List

import read_data


def solve_part_1(data: List[int]) -> int:
    nums = get_nums(data)
    rearranged = rearrange(nums)
    return get_checksum(rearranged)


def solve_part_2(data: List[int]) -> int:
    nums = get_nums(data)
    rearranged = rearrange_2(nums)
    return get_checksum(rearranged)


def rearrange(nums: List[int | str]) -> List[int | str]:
    spaces = []
    for i, n in enumerate(nums):
        if n == '.':
            spaces.append(i)
    j = 0
    for i, n in enumerate(nums[::-1]):
        if n != '.':
            nums[~i], nums[spaces[j]] = nums[spaces[j]], nums[~i]
            j += 1
            to_move = sum(1 for n in nums[nums.index('.') + 1:] if n != '.')
            if j >= len(spaces) or to_move == 0:
                break
    return nums


def find_group_id(nums: List[List[int | str]], gr_id: int) -> int:
    for i, gr in enumerate(nums):
        if gr[0] == gr_id:
            return i
    return -1


def rearrange_2(nums: List[int]) -> List[int | str]:
    nums = group_consecutive(nums)
    ids = set(chain.from_iterable(nums))
    ids.remove('.')
    spaces = get_spaces_indices(nums)
    for n in sorted(ids, reverse=True):
        i = find_group_id(nums, n)
        nums = move_group(nums, spaces, i)
        spaces = get_spaces_indices(nums)
    nums = list(chain.from_iterable(nums))
    return nums


def get_nums(data: List[int]) -> List[int | str]:
    nums = []
    for i, n in enumerate(data):
        if i % 2 == 0:
            nums.extend([i // 2] * n)
        else:
            nums.extend('.' * n)
    return nums


def group_consecutive(nums: List[int | str]) -> List[List[int | str]]:
    grouped, t = [], []
    for i, n in enumerate(nums):
        if not t or t[0] == n:
            t.append(n)
        else:
            grouped.append(t)
            t = [n]
    if t:
        grouped.append(t)
    return grouped


def move_group(nums: List[List[int | str]], space_indices: List[int], gr_index: int) -> List[List[int | str]]:
    for s_i in space_indices:
        if s_i >= gr_index:
            return nums
        l1, l2 = len(nums[s_i]), len(nums[gr_index])
        if l1 >= l2:
            nums[gr_index], nums[s_i] = ['.' for _ in range(l2)], nums[gr_index]
            if l1 - l2 > 0:
                nums.insert(s_i + 1, ['.' for _ in range(l1 - l2)])
            nums = list(chain.from_iterable(nums))
            nums = group_consecutive(nums)
            return nums
    return nums


def get_spaces_indices(nums: List[List[int | str]]) -> List[int]:
    return [i for i, gr in enumerate(nums) if gr[0] == '.']


def get_checksum(nums: List[int | str]) -> int:
    return sum(i * n for i, n in enumerate(nums) if n != '.')


if __name__ == '__main__':
    sample = [int(n) for n in read_data.get_data_00('sample.txt')]
    my_input = [int(n) for n in read_data.get_data_00('input.txt')]

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
