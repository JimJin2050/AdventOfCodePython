# -*- coding: utf-8 -*-


def count_of_visible_dot_after_first_fold(coordinate_list, fold_info_list) -> int:
    dot_list = fold_transparent_paper(coordinate_list, fold_info_list[0])
    return len(dot_list)


def print_activate_code(dot_list, fold_info_list):
    for fold in fold_info_list:
        dot_list = fold_transparent_paper(dot_list, fold)

    max_row = max([dot[1] for dot in dot_list]) + 1
    max_col = max([dot[0] for dot in dot_list]) + 1

    matrix = [['#' if (i, j) in dot_list else '.' for i in range(max_col)] for j in range(max_row)]

    for row in matrix:
        print("".join(row))


def fold_transparent_paper(coordinate_list, fold_info) -> list:
    fold_axis, value = fold_info.split("=")
    fold_value = int(value)
    dot_list = []
    for idx, dot in enumerate(coordinate_list):
        x, y = list(map(int, dot))
        if fold_axis == "y":
            if y != fold_value and y <= 2 * fold_value:
                dot_list.append([x, y if y < fold_value else 2 * fold_value - y])
        else:
            if x != fold_value and x <= 2 * fold_value:
                dot_list.append([x if x < fold_value else 2 * fold_value - x, y])

    return list(set([tuple(dot) for dot in dot_list]))


if __name__ == "__main__":
    # read data
    with open("data/day13_input.txt") as f:
        data_list = f.readlines()

    # parse data
    dot_coordinate_list, fold_list = [], []
    for line in data_list:
        if line.strip():
            if "fold" in line:
                fold_list.append(line.strip().split()[-1])
            else:
                dot_coordinate_list.append(tuple(map(int, line.strip().split(","))))

    # part1
    print("Answer of part 1:")
    print(count_of_visible_dot_after_first_fold(dot_coordinate_list, fold_list))

    # part2
    print("Answer of part 2:")
    print_activate_code(dot_coordinate_list, fold_list)
