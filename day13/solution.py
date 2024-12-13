"""
Challenge Link: https://adventofcode.com/2024/day/13

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import typing

import sympy as sp

import read_data


def solve(data: typing.List[typing.List[int]], incr: int = 0) -> int:
    data = [(data[i:i + 3]) for i in range(0, len(data), 4)]
    token_a_cost = 3
    token_b_cost = 1
    total_cost = 0

    for (ax, ay), (bx, by), (X, Y) in data:
        press_a, press_b = sp.symbols('press_a, press_b')

        eq1 = sp.Eq(ax * press_a + bx * press_b, X + incr)
        eq2 = sp.Eq(ay * press_a + by * press_b, Y + incr)

        d = sp.solvers.solve([eq1, eq2], dict=True)[0]
        cost = d[press_a] * token_a_cost + d[press_b] * token_b_cost
        valid = any((incr > 0, incr == 0 and all(p < 100 for p in [d[press_a], d[press_b]])))

        if valid and int(cost) == cost:
            total_cost += cost

    return total_cost


if __name__ == '__main__':
    sample = read_data.get_data_09_all_line_ints('sample.txt')
    my_input = read_data.get_data_09_all_line_ints('input.txt')
    part_2_increment = 10000000000000

    example_1 = solve(sample)
    part_1 = solve(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve(sample, part_2_increment)
    part_2 = solve(my_input, part_2_increment)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
