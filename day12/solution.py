"""
Challenge Link: https://adventofcode.com/2024/day/12

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import read_data


def solve(data: typing.List[str]) -> typing.Tuple[int, int]:
    visited = set()
    r1, r2 = 0, 0
    for a in range(len(data)):
        for b in range(len(data[a])):
            area = 1
            if (a, b) not in visited:
                togo = [(a, b)]
                region_points = set()
                while togo:
                    x, y = togo.pop()
                    visited.add((x, y))
                    region_points.add((x, y))
                    neighbours = [(i, j) for i, j in get_neighbours(x, y, data) if
                                  (i, j) not in visited and data[i][j] == data[x][y]]
                    area += len(neighbours)
                    visited.update(neighbours)
                    togo.extend(neighbours)
                r1 += (area * calc_perimeter(region_points))
                r2 += (area * calc_sides(region_points))
    return r1, r2


def get_neighbours(i: int, j: int, data: typing.List[str]) -> typing.List[typing.Tuple[int, int]]:
    return [(i + h, j + v) for h, v in [(0, 1), (1, 0), (-1, 0), (0, -1)] if is_in_area(data, i + h, j + v)]


def get_potential_neighbours(i: int, j: int) -> typing.List[typing.Tuple[int, int]]:
    return [(i + h, j + v) for h, v in [(0, 1), (1, 0), (-1, 0), (0, -1)]]


def is_in_area(data: typing.List[str], i: int, j: int) -> bool:
    if not 0 <= i < len(data):
        return False
    if not 0 <= j < len(data[0]):
        return False
    return True


def calc_perimeter(area_points: typing.Set[typing.Tuple[int, int]]) -> int:
    return sum(1 for x, y in area_points for neigh in get_potential_neighbours(x, y) if neigh not in area_points)


def calc_sides(area_points: typing.Set[typing.Tuple[int, int]]) -> int:
    upper, lower, right, left = set(), set(), set(), set()
    for x, y in area_points:
        if (x - 1, y) not in area_points:
            upper.add((x - 1, y))
        if (x + 1, y) not in area_points:
            lower.add((x + 1, y))
        if (x, y - 1) not in area_points:
            left.add((x, y - 1))
        if (x, y + 1) not in area_points:
            right.add((x, y + 1))
    upper = sorted(upper)
    lower = sorted(lower)
    left = sorted(left, key=lambda p: (p[1], p[0]))
    right = sorted(right, key=lambda p: (p[1], p[0]))
    horizontal_sides_cnt = sum(get_consecutive_cnt(level) for level in [upper, lower])
    vertical_sides_cnt = sum(get_consecutive_cnt(level, 1) for level in [left, right])
    return horizontal_sides_cnt + vertical_sides_cnt


def get_consecutive_cnt(sorted_points: typing.List[typing.Tuple[int, int]], axis: int = 0) -> int:
    axis_2 = 0 if axis == 1 else 1
    cur_1 = sorted_points[0][axis]
    cur_2 = sorted_points[0][axis_2]
    cnt = 1
    for p in sorted_points[1:]:
        if (p[axis] != cur_1) or (p[axis] == cur_1 and p[axis_2] - 1 != cur_2):
            cnt += 1
        cur_1 = p[axis]
        cur_2 = p[axis_2]
    return cnt


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1, example_2 = solve(sample)
    part_1, part_2 = solve(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
