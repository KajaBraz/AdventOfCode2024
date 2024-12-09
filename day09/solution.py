"""
Challenge Link: https://adventofcode.com/2024/day/9

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import re

import read_data


def solve_part_1(data) -> int:
    rearranged = rearrange(data)
    return get_checksum(rearranged)


def rearrange(nums):
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


def rearrange_2(nums):
    # Improvements in progress
    # TODO: change logic, refactor, improve execution time

    spaces = re.finditer(r'\.+', ''.join([str(s) for s in nums]))
    spaces = [(sp.start(), sp.end()) for sp in spaces]
    cant_move = 0
    i, j = 0, 0
    while i < len(nums) and sum(1 for n in nums[nums.index('.') + 1:] if n != '.') - cant_move >= 0:
        n = nums[~i]
        if n == '.':
            i += 1
            continue
        cur = re.search(fr'{n}+', ''.join([str(s) for s in nums]))
        s, e = cur.start(), cur.end()
        i = i + (e - s)
        placed = False
        j = 0
        while j < len(spaces) and not placed:
            sp_s, sp_e = spaces[j]
            if e - s > sp_e - sp_s:
                j += 1
            else:
                diff = (sp_e - sp_s) - (e - s)
                nums[s:e], nums[sp_s:sp_e - diff] = nums[sp_s:sp_e][:e - s], nums[s:e]
                if diff == 0:
                    spaces.pop(j)
                else:
                    spaces[j] = (sp_s + (e - s), sp_e - diff + 1)
                placed = True
        if not placed:
            cant_move += (e - s)
    return nums


def solve_part_2(data) -> int:
    rearranged = rearrange_2(data)
    return get_checksum(rearranged)


def get_nums(data):
    nums = []
    for i, n in enumerate(data):
        if i % 2 == 0:
            nums.extend([i // 2] * n)
        else:
            nums.extend('.' * n)
    return nums


def get_checksum(nums):
    r = 0
    for i, n in enumerate(nums):
        if n != '.':
            r += (i * n)
    return r


if __name__ == '__main__':
    sample = get_nums([int(n) for n in read_data.get_data_00('sample.txt')])
    my_input = get_nums([int(n) for n in read_data.get_data_00('input.txt')])

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    # example_2 = solve_part_2(sample)
    # part_2 = solve_part_2(my_input)
    # print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
