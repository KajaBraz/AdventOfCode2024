"""
Challenge Link: https://adventofcode.com/2024/day/20

Paste sample and your input in the dedicated files and run the code to see the results.
"""

from typing import Dict, List, Tuple, Set

import read_data


def solve(data: List[str], d: int) -> int:
    s, e = get_start_end(data)
    cnt = 0
    distances_from_start = get_distances(e, s, data)
    distances_to_end = get_distances(s, e, data)
    no_cheat_time = distances_to_end[s]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '#':
                out_of_wall = get_through_wall((i, j), data, d)
                for x, y, wall_len in out_of_wall:
                    d_before_wall = distances_from_start[(i, j)]
                    d_after_wall = distances_to_end[(x, y)]
                    cheat_time = d_before_wall + wall_len + d_after_wall
                    if cheat_time <= no_cheat_time - 100:
                        cnt += 1
    return cnt


def get_distances(from_p: Tuple[int, int], to_p: Tuple[int, int], area: List[str]) -> Dict[Tuple[int, int], int]:
    i, j = to_p
    d = 0
    distances = {to_p: 0}
    while (i, j) != from_p:
        neighs = [n for n in get_neighbours(i, j, area) if area[n[0]][n[1]] != '#' and n not in distances]
        if neighs:
            i, j = neighs[0]
            d += 1
            distances[(i, j)] = d
    return distances


def get_start_end(data: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    s, e = (-1, -1), (-1, -1)
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == 'S':
                s = (i, j)
            elif cell == 'E':
                e = (i, j)
    return s, e


def get_neighbours(i: int, j: int, area) -> List[Tuple[int, int]]:
    area_size = (len(area), len(area[0]))
    n = [(i + h, j + v) for h, v in [(0, 1), (1, 0), (-1, 0), (0, -1)] if is_in_area(area_size, i + h, j + v)]
    return n


def is_in_area(area_size, x: int, y: int) -> bool:
    return 0 <= x < area_size[0] and 0 <= y < area_size[1]


def get_through_wall(start_p: Tuple[int, int], area: List[str], d: int) -> Set[Tuple[int, int, int]]:
    si, sj = start_p
    out_of_wall = set()
    for i in range(d + 1):
        for j in range(d + 1 - i):
            if is_in_area((len(area), len(area[0])), si + i, sj + j) and area[si + i][sj + j] != '#':
                out_of_wall.add((si + i, sj + j, i + j))
            if is_in_area((len(area), len(area[0])), si - i, sj + j) and area[si - i][sj + j] != '#':
                out_of_wall.add((si - i, sj + j, i + j))
            if is_in_area((len(area), len(area[0])), si + i, sj - j) and area[si + i][sj - j] != '#':
                out_of_wall.add((si + i, sj - j, i + j))
            if is_in_area((len(area), len(area[0])), si - i, sj - j) and area[si - i][sj - j] != '#':
                out_of_wall.add((si - i, sj - j, i + j))
    return out_of_wall


if __name__ == '__main__':
    my_input = read_data.get_data_02_str_list('input.txt')

    part_1 = solve(my_input, 2)
    print(f'Part 1 Solution: {part_1}')

    part_2 = solve(my_input, 20)
    print(f'Part 2 Solution: {part_2}')
