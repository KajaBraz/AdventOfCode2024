"""
Challenge Link: https://adventofcode.com/2024/day/10

Paste sample and your input in the dedicated files and run the code to see the results.
"""

from typing import List, Tuple

import read_data


def solve_part_1(data: List[str]) -> int:
    data = [[int(s) for s in row] for row in data]
    trailheads = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 0]
    return sum(get_trailhead_score(head, data) for head in trailheads)


def solve_part_2(data: List[str]) -> int:
    data = [[int(s) for s in row] for row in data]
    trailheads = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 0]
    return sum(get_trailhead_rating(head, data) for head in trailheads)


def get_trailhead_score(head: Tuple[int, int], data: List[List[int]], distinct: bool = False) -> int:
    score, visited = 0, set()
    togo = [head]
    while togo:
        i, j = togo.pop()
        if not distinct and (i, j) in visited:
            continue
        visited.add((i, j))
        v = data[i][j]
        if v == 9:
            score += 1
        neighs = [p for p in get_neighbours(i, j, data) if data[p[0]][p[1]] == v + 1]
        togo.extend(neighs)
    return score


def get_trailhead_rating(head: Tuple[int, int], data: List[List[int]]) -> int:
    return get_trailhead_score(head, data, True)


def get_neighbours(i: int, j: int, data: List[List[int]]) -> List[Tuple[int, int]]:
    return [(i + h, j + v) for h, v in [(0, 1), (1, 0), (-1, 0), (0, -1)] if is_in_area(data, i + h, j + v)]


def is_in_area(data: List[List[int]], i: int, j: int) -> bool:
    if not 0 <= i < len(data):
        return False
    if not 0 <= j < len(data[0]):
        return False
    return True


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
