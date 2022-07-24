# -*- coding: utf-8 -*-
import copy

# read data
with open("data/day11_input.txt") as f:
    data_list = f.readlines()

octopus_energy_level_matrix = [list(map(int, list(line.strip()))) for line in data_list]
octopus_energy_level_matrix_1 = copy.deepcopy(octopus_energy_level_matrix)
octopus_energy_level_matrix_2 = copy.deepcopy(octopus_energy_level_matrix)

rows, cols = len(octopus_energy_level_matrix), len(octopus_energy_level_matrix[0])


# part 1
def calculate_total_flashes(matrix, steps):
    total = 0
    for step in range(steps):
        total += step_total_flashes(matrix)
    return total


# part 2
def calculate_all_sync_flash_steps(matrix):
    steps = 0
    while True:
        steps += 1
        if 100 == step_total_flashes(matrix):
            return steps


def step_total_flashes(matrix):
    step_count = 0
    matrix_increase(matrix)
    flag_matrix = [[True for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            adjacent_octopus_increase(col, row, matrix, flag_matrix)

    for row in range(rows):
        for col in range(cols):
            if matrix[col][row] > 9:
                matrix[col][row] = 0
                step_count += 1

    return step_count


def matrix_increase(matrix):
    for row in range(rows):
        for col in range(cols):
            matrix[col][row] += 1


def adjacent_octopus_increase(col, row, matrix, flag_matrix):
    if flag_matrix[col][row] and matrix[col][row] > 9:
        flag_matrix[col][row] = False
        if row - 1 >= 0:
            matrix[col][row - 1] += 1
            adjacent_octopus_increase(col, row - 1, matrix, flag_matrix)
        if col - 1 >= 0 and row - 1 >= 0:
            matrix[col - 1][row - 1] += 1
            adjacent_octopus_increase(col - 1, row - 1, matrix, flag_matrix)
        if col + 1 < cols and row - 1 >= 0:
            matrix[col + 1][row - 1] += 1
            adjacent_octopus_increase(col + 1, row - 1, matrix, flag_matrix)
        if col - 1 >= 0:
            matrix[col - 1][row] += 1
            adjacent_octopus_increase(col - 1, row, matrix, flag_matrix)
        if row + 1 < rows:
            matrix[col][row + 1] += 1
            adjacent_octopus_increase(col, row + 1, matrix, flag_matrix)
        if col - 1 >= 0 and row + 1 < rows:
            matrix[col - 1][row + 1] += 1
            adjacent_octopus_increase(col - 1, row + 1, matrix, flag_matrix)
        if col + 1 < cols and row + 1 < rows:
            matrix[col + 1][row + 1] += 1
            adjacent_octopus_increase(col + 1, row + 1, matrix, flag_matrix)
        if col + 1 < cols:
            matrix[col + 1][row] += 1
            adjacent_octopus_increase(col + 1, row, matrix, flag_matrix)


if __name__ == "__main__":
    print("Total flashes is {}".format(calculate_total_flashes(octopus_energy_level_matrix_1, 100)))
    print(calculate_all_sync_flash_steps(octopus_energy_level_matrix_2))

