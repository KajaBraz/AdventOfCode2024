"""
Challenge Link: https://adventofcode.com/2024/day/16

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections
import heapq
from typing import List, Tuple, Set, Callable

import read_data

DIR_INCR = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
DIR_ROTATION = {'N': ('E', 'W'), 'S': ('E', 'W'), 'E': ('N', 'S'), 'W': ('N', 'S')}
MOVE_COST = 1
ROTATION_COST = 1000


def solve_part_1(data: List[str]) -> int:
    s, e = get_start_end(data)
    visited_costs = go_dijkstra(data, s)
    final_cost = min(visited_costs[(*e, direction)] for direction in 'NSEW' if (*e, direction) in visited_costs)
    return final_cost


def solve_part_2(data: List[str]) -> int:
    s, e = get_start_end(data)
    visited_costs = go_dijkstra(data, s)
    final_cost = min(visited_costs[(*e, direction)] for direction in 'NSEW' if (*e, direction) in visited_costs)
    return len(go_dijkstra_backwards(data, e, visited_costs, final_cost))


def get_start_end(data: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    s = -1, -1
    e = -1, -1
    for i in range(len(data)):
        for j, cell in enumerate(data[i]):
            if cell == 'S':
                s = (i, j)
            elif cell == 'E':
                e = (i, j)
    return s, e


def go_dijkstra(data: List[str], start_p: Tuple[int, int]) -> collections.defaultdict[Tuple[int, int, str], int]:
    x, y = start_p
    togo = [(0, x, y, 'E')]
    visited = collections.defaultdict(lambda: 1000000)
    visited[(x, y, 'E')] = 0
    heapq.heapify(togo)

    while togo:
        cost, x, y, direction = heapq.heappop(togo)

        can_move_horizontal, next_step = move_horizontal(data, cost, x, y, direction, visited)
        if can_move_horizontal:
            visited[next_step] = cost + MOVE_COST
            heapq.heappush(togo, (cost + MOVE_COST, next_step[0], next_step[1], direction))

        for rotation_step in rotate(cost, x, y, direction, visited):
            visited[rotation_step] = cost + ROTATION_COST
            heapq.heappush(togo, (cost + ROTATION_COST, x, y, rotation_step[-1]))

    return visited


def go_dijkstra_backwards(data: List[str], end_p: Tuple[int, int],
                          visited: collections.defaultdict[Tuple[int, int, str], int],
                          final_cost: int) -> Set[Tuple[int, int]]:
    togo = [(end_p[0], end_p[1], d) for d in 'NSEW' if visited[(end_p[0], end_p[1], d)] == final_cost]
    shortest_paths_points = set(togo)
    heapq.heapify(togo)

    while togo:
        x, y, direction = heapq.heappop(togo)
        cost = visited[(x, y, direction)]

        can_move_horizontal, step_back = move_horizontal(data, cost, x, y, direction, visited, lambda a, b: a - b)
        if can_move_horizontal:
            if step_back not in shortest_paths_points:
                if cost - MOVE_COST == visited[step_back]:
                    shortest_paths_points.add(step_back)
                    heapq.heappush(togo, step_back)

        for step_rotated_back in rotate(cost, x, y, direction, visited, lambda a, b: a - b):
            if visited[step_rotated_back] == cost - ROTATION_COST:
                if step_rotated_back not in shortest_paths_points:
                    shortest_paths_points.add(step_rotated_back)
                    heapq.heappush(togo, step_rotated_back)

    return {(x, y) for (x, y, _) in shortest_paths_points}


def move_horizontal(data: List[str], cur_cost: int, cur_x: int, cur_y: int, cur_dir: str,
                    visited_costs: collections.defaultdict[Tuple[int, int, str], int],
                    operation: Callable = lambda a, b: a + b) -> Tuple[bool, Tuple[int, int, str] | Tuple]:
    incr = DIR_INCR[cur_dir]
    x, y = operation(cur_x, incr[0]), operation(cur_y, incr[1])
    if is_in_area(data, x, y) and data[x][y] != '#':
        next_step = (x, y, cur_dir)
        if 0 <= operation(cur_cost, MOVE_COST) <= visited_costs[next_step]:
            return True, next_step
    return False, ()


def rotate(cur_cost: int, cur_x: int, cur_y: int, cur_dir: str,
           visited_costs: collections.defaultdict[Tuple[int, int, str], int],
           operation: Callable = lambda a, b: a + b) -> List[Tuple[int, int, str]]:
    next_steps = []
    for rotated_dir in DIR_ROTATION[cur_dir]:
        next_step = (cur_x, cur_y, rotated_dir)
        if 0 <= operation(cur_cost, ROTATION_COST) <= visited_costs[next_step]:
            next_steps.append(next_step)
    return next_steps


def is_in_area(data: List[str], x: int, y: int) -> bool:
    return 0 <= x < len(data) and 0 <= y < len(data[x])


if __name__ == '__main__':
    sample_1 = read_data.get_data_02_str_list('sample_1.txt')
    sample_2 = read_data.get_data_02_str_list('sample_2.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1_1 = solve_part_1(sample_1)
    example_2_1 = solve_part_1(sample_2)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExamples: {example_1_1}; {example_2_1} | Solution: {part_1}')

    example_1_2 = solve_part_2(sample_1)
    example_2_2 = solve_part_2(sample_2)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExamples: {example_1_2}; {example_2_2} | Solution: {part_2}')
