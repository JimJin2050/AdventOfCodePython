# -*- coding: utf-8 -*-
import math


# Part 1
def align_to_position_with_least_fuel_under_constant_rate(init_positions):
    return min([sum([abs(init_p - pos) for init_p in init_positions]) for pos in range(len(init_positions))])


# part 2
def align_to_position_with_least_fuel_under_non_constant_rate(init_positions):
    min_fuel_cost = float('inf')
    for position in range(len(init_positions)):
        fuel_cost = 0
        for init_p in init_positions:
            distance = abs(init_p - position)
            if distance % 2 == 0:
                fuel_cost += (distance + 1) * math.floor(distance/2)
            else:
                fuel_cost += distance * math.ceil(distance/2)

        min_fuel_cost = fuel_cost if min_fuel_cost > fuel_cost else min_fuel_cost

    return min_fuel_cost


if __name__ == "__main__":
    # read data
    with open("data/day7_input.txt") as f:
        data_list = f.readlines()

    positions = [int(position) for position in data_list[0].split(",")]

    print(align_to_position_with_least_fuel_under_constant_rate(positions))
    print(align_to_position_with_least_fuel_under_non_constant_rate(positions))
