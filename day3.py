# -*- coding: utf-8 -*-
import numpy
import copy


# Part 1
def calculate_power_consumption():
    with open("data/day3_input.txt") as f:
        data_list = f.readlines()
    data_2d_list = [[int(char) for char in line.strip()] for line in data_list]
    data_2d_array = numpy.array(data_2d_list)

    gamma_rate, epsilon_rate = "", ""
    rows_len, cols_len = len(data_2d_list), len(data_2d_list[0])
    for idx in range(cols_len):
        if sum(data_2d_array[:, idx]) > rows_len/2:
            gamma_rate, epsilon_rate = gamma_rate + "1", epsilon_rate + "0"
        else:
            gamma_rate, epsilon_rate = gamma_rate + "0", epsilon_rate + "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


# Part 2
def calculate_life_support_rating():
    with open("data/day3_input.txt") as f:
        data_list = f.readlines()
    data_2d_list = [[int(char) for char in line.strip()] for line in data_list]

    rows_len, cols_len = len(data_2d_list), len(data_2d_list[0])
    oxygen_remained, co2_remained = copy.deepcopy(data_2d_list), copy.deepcopy(data_2d_list)

    for col in range(cols_len):
        if len(oxygen_remained) > 1:
            if sum([row[col] for row in oxygen_remained]) >= len(oxygen_remained)/2:
                oxygen_remained = [row for row in oxygen_remained if row[col] == 1]
            else:
                oxygen_remained = [row for row in oxygen_remained if row[col] == 0]

        if len(co2_remained) > 1:
            if sum([row[col] for row in co2_remained]) >= len(co2_remained)/2:
                co2_remained = [row for row in co2_remained if row[col] == 0]
            else:
                co2_remained = [row for row in co2_remained if row[col] == 1]

    oxygen_rate, co2_rate = "".join([str(d) for d in oxygen_remained[0]]), "".join([str(d) for d in co2_remained[0]])
    return int(oxygen_rate, 2) * int(co2_rate, 2)


if __name__ == "__main__":
    print(calculate_power_consumption())
    print(calculate_life_support_rating())
