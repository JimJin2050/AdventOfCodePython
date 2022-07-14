# -*- coding: utf-8 -*-
def how_many_measurements_larger_than_previous():
    with open("data/day1_input.txt") as depth_f:
        depths = depth_f.readlines()

    return count_of_increased_value_in_list(depths)


def how_many_sums_larger_than_previous():
    with open("data/day1_input.txt") as depth_f:
        depths = depth_f.readlines()

    depths_len = len(depths)
    if depths_len < 3:
        raise AssertionError("Incorrect input data!")

    measurements = [int(depths[idx]) + int(depths[idx-1]) + int(depths[idx-2]) for idx in range(2, depths_len)]

    return count_of_increased_value_in_list(measurements)


def count_of_increased_value_in_list(input_list):
    length = len(input_list)
    if length < 2:
        return 0

    count = 0
    for idx in range(1, length):
        count = count + 1 if int(input_list[idx]) > int(input_list[idx - 1]) else count

    return count


if __name__ == "__main__":
    print(how_many_measurements_larger_than_previous())
    print(how_many_sums_larger_than_previous())
