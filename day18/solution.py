"""
Challenge Link: https://adventofcode.com/2024/day/18

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections
import heapq
from typing import List, Tuple, Set

import read_data


def solve_part_1(data: List[List[int]], area_size: Tuple[int, int], discard_at: int) -> int:
    corrupted = {(x, y) for x, y in data[:discard_at]}
    v = go_dijkstra((0, 0), corrupted, area_size)
    return v


def solve_part_2(data: List[List[int]], area_size: Tuple[int, int]) -> str:
    corrupted = set()
    for x, y in data:
        corrupted.add((x, y))
        steps = go_dijkstra((0, 0), corrupted, area_size)
        if steps == -1:
            return f'{x},{y}'
        corrupted.add((x, y))
    return ''


def get_neighbours(i: int, j: int, area_size: Tuple[int, int]) -> List[Tuple[int, int]]:
    return [(i + h, j + v) for h, v in [(0, 1), (1, 0), (-1, 0), (0, -1)] if is_in_area(area_size, i + h, j + v)]


def is_in_area(area_size, x: int, y: int) -> bool:
    return 0 <= x <= area_size[0] and 0 <= y <= area_size[1]


def go_dijkstra(start_p: Tuple[int, int], corrupted: Set[Tuple[int, int]], area_size: Tuple[int, int]) -> int:
    x, y = start_p
    togo = [(0, x, y)]
    visited = collections.defaultdict(lambda: 1_000_000)
    visited[(x, y)] = 0
    heapq.heapify(togo)

    while togo:
        cost, x, y = heapq.heappop(togo)
        if (x, y) == area_size:
            return cost

        visited[(x, y)] = cost
        neighs = [neigh for neigh in get_neighbours(x, y, area_size) if neigh not in corrupted and neigh not in visited]
        for neigh in neighs:
            new_cost = min(cost + 1, visited[neigh])
            if cost + 1 < visited[neigh]:
                heapq.heappush(togo, (new_cost, neigh[0], neigh[1]))

    return -1


if __name__ == '__main__':
    sample = read_data.get_data_09_all_line_ints('sample.txt')
    my_input = read_data.get_data_09_all_line_ints('input.txt')

    example_1 = solve_part_1(sample, (6, 6), 12)
    part_1 = solve_part_1(my_input, (70, 70), 1024)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample, (6, 6))
    part_2 = solve_part_2(my_input, (70, 70))
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
