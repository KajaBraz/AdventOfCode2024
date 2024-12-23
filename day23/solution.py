"""
Challenge Link: https://adventofcode.com/2024/day/23

Paste sample and your input in the dedicated files and run the code to see the results.
"""

import collections
import typing

import networkx

import read_data


def solve(data: typing.List[str]) -> typing.Tuple[int, str]:
    data = [row.split('-') for row in data]
    computers = networkx.Graph()
    for c1, c2 in data:
        computers.add_edge(c1, c2)
    all_adj = list(networkx.enumerate_all_cliques(computers))
    triplets = [adj for adj in all_adj if len(adj) == 3]
    part_1_solution = sum(any_starts_with_char(triplet, 't') for triplet in triplets)
    part_2_solution = ','.join(sorted(all_adj[-1]))
    return part_1_solution, part_2_solution


def any_starts_with_char(strs: typing.Iterable[str], char: str) -> bool:
    return True if any(s[0] == char for s in strs) else False


def solve_part_1_alternative(data: typing.List[str]) -> int:
    data = [row.split('-') for row in data]
    d = collections.defaultdict(set)
    for c1, c2 in data:
        d[c1].add(c2)
        d[c2].add(c1)
    triplets = set()
    for comp, comps in d.items():
        for comp2, comps2 in d.items():
            for comp3, comps3 in d.items():
                if comp != comp2 != comp3:
                    t = tuple(sorted([comp, comp2, comp3]))
                    if t not in triplets:
                        if comp in comps2 and comp in comps3:
                            if comp2 in comps and comp2 in comps3:
                                if comp3 in comps and comp3 in comps2:
                                    triplets.add(t)
    return sum(any_starts_with_char(triplet, 't') for triplet in triplets)


if __name__ == '__main__':
    sample = read_data.get_data_02_str_list('sample.txt')
    my_input = read_data.get_data_02_str_list('input.txt')

    example_1, example_2 = solve(sample)
    part_1, part_2 = solve(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
