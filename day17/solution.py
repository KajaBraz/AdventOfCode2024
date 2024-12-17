"""
Challenge Link: https://adventofcode.com/2024/day/17

Paste sample and your input in the dedicated files and run the code to see the results.
"""

from typing import List

import read_data


def solve_part_1(data: List[List[int]]) -> str:
    a_register, b_register, c_register = [x[0] for x in data[:3]]
    program = data[-1]
    return ','.join(str(n) for n in execute_instructions(program, a_register, b_register, c_register))


def execute_instructions(program: List[int], a_register: int, b_register: int, c_register: int) -> List[int]:
    pointer, output = 0, []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        combo_operand = get_combo_operand(operand, a_register, b_register, c_register)
        special_pointer_move = False
        if opcode == 0:
            a_register = a_register // 2 ** combo_operand
        elif opcode == 1:
            b_register = b_register ^ operand
        elif opcode == 2:
            b_register = combo_operand % 8
        elif opcode == 3:
            if a_register != 0:
                special_pointer_move = True
                pointer = operand
        elif opcode == 4:
            b_register = b_register ^ c_register
        elif opcode == 5:
            output.append(int(combo_operand % 8))
        elif opcode == 6:
            b_register = a_register // 2 ** combo_operand
        elif opcode == 7:
            c_register = a_register // 2 ** combo_operand
        if not special_pointer_move:
            pointer += 2
    return output


def get_combo_operand(operand: int, reg_a: int, reg_b: int, reg_c: int) -> int:
    if operand <= 3:
        return operand
    return reg_a if operand == 4 else reg_b if operand == 5 else reg_c if operand == 6 else -1


def find_lowest_register_a(program: List[int], from_i: int, temp: int, level: int) -> int:
    if level < 0:
        return temp
    potential_as = [a for a in range(from_i, from_i + 8) if execute_instructions(program, a, 0, 0)[0] == program[level]]
    for a in potential_as:
        lowest_a = find_lowest_register_a(program, get_next_nums_range_start_i(a), a, level - 1)
        if lowest_a != -1:
            return lowest_a
    return -1


def get_next_nums_range_start_i(i: int) -> int:
    return i * 8


def solve_part_2(data: List[List[int]]) -> int:
    program = data[-1]
    return find_lowest_register_a(program, 0, 0, len(program) - 1)


if __name__ == '__main__':
    sample_1 = read_data.get_data_09_all_line_ints('sample_1.txt')
    sample_2 = read_data.get_data_09_all_line_ints('sample_2.txt')
    my_input = read_data.get_data_09_all_line_ints('input.txt')

    example_1 = solve_part_1(sample_1)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample_2)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
