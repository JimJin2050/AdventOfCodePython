# -*- coding: utf-8 -*-


def multiply_of_final_horizontal_position_by_final_depth():
    with open("data/day2_input.txt") as f:
        data_list = f.readlines()

    position, depth = 0, 0
    for data in data_list:
        command, x_units = data.split()[0], int(data.split()[1])
        if command == "forward":
            position += x_units
        elif command == "down":
            depth += x_units
        elif command == "up":
            depth = depth - x_units if (depth - x_units) > 0 else 0
        else:
            raise AssertionError("Invalid command!")

    return position * depth


def multiply_of_final_horizontal_position_by_final_depth_has_aim():
    with open("data/day2_input.txt") as f:
        data_list = f.readlines()

    position, depth, aim = 0, 0, 0
    for data in data_list:
        command, x_units = data.split()[0], int(data.split()[1])
        if command == "forward":
            position += x_units
            depth += aim * x_units
        elif command == "down":
            aim += x_units
        elif command == "up":
            aim = aim - x_units if (aim - x_units) > 0 else 0
        else:
            raise AssertionError("Invalid command!")

    return position * depth


if __name__ == "__main__":
    print(multiply_of_final_horizontal_position_by_final_depth())
    print(multiply_of_final_horizontal_position_by_final_depth_has_aim())
