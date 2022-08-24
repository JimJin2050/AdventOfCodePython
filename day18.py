# -*- coding: utf-8 -*-
import re
import math


def explode(snail_fish_number: str) -> str:
    for match in re.finditer(r"\[(\d*),(\d*)\]", snail_fish_number):
        start_index, end_index = match.span()
        left = snail_fish_number[0:start_index]
        right = snail_fish_number[end_index:]

        if list(left).count('[') - list(left).count(']') >= 4:
            list_left_num, list_right_num = eval(match.group())

            if re.search(r"\d+", left):
                left_num_match = list(re.finditer(r"\d+", left))[-1]
                left_nearest_num = int(left_num_match.group())
                left = "{}{}{}".format(
                    left[:left_num_match.span()[0]],
                    str(left_nearest_num + list_left_num),
                    left[left_num_match.span()[1]:]
                )
            if re.search(r"\d+", right):
                right_num_match = list(re.finditer(r"\d+", right))[0]
                right_nearest_num = int(right_num_match.group())
                right = "{}{}{}".format(
                    right[:right_num_match.span()[0]],
                    str(right_nearest_num + list_right_num),
                    right[right_num_match.span()[1]:]
                )

            return left + '0' + right
    else:
        return ""


def split(snail_fish_number: str) -> str:
    match = re.search(r"\d{2}", snail_fish_number)

    if match:
        split_num = int(match.group())
        start, end = match.span()
        replace_str = "[{},{}]".format(math.floor(split_num/2), math.ceil(split_num/2))
        return snail_fish_number[:start] + replace_str + snail_fish_number[end:]
    else:
        return ""


def reduce(snail_fish_number: str) -> str:
    while True:
        new_pair = explode(snail_fish_number)
        if not new_pair:
            new_pair = split(snail_fish_number)
        if not new_pair:
            break
        snail_fish_number = new_pair
    return snail_fish_number


def add_up_pair_list(snail_fish_number_lines: list) -> str:
    reduced_number = snail_fish_number_lines[0].strip()
    for index in range(1, len(snail_fish_number_lines)):
        line = snail_fish_number_lines[index].strip()
        reduced_number = reduce("[{},{}]".format(reduced_number, line))

    return reduced_number


def magnitude(number_list: list) -> int:
    if all([
        isinstance(number_list[0], int),
        isinstance(number_list[1], int)
    ]):
        return 3 * number_list[0] + 2 * number_list[1]
    elif isinstance(number_list[0], int) and isinstance(number_list[1], list):
        return 3 * number_list[0] + 2 * magnitude(number_list[1])
    elif isinstance(number_list[1], int) and isinstance(number_list[0], list):
        return 3 * magnitude(number_list[0]) + 2 * number_list[1]
    else:
        return 3 * magnitude(number_list[0]) + 2 * magnitude(number_list[1])


def get_maximum_magnitude(number_list: list) -> int:
    maximum = 0
    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if i != j:
                maximum = max(
                    maximum,
                    magnitude(eval(add_up_pair_list([number_list[i], number_list[j]]))))

    return maximum


def main():
    # read data
    with open("data/day18_input.txt") as f:
        data_list = f.readlines()

    lines = [line.strip() for line in data_list]

    # Answer of part 1
    print("Magnitude of the final sum: {}".format(magnitude(eval(add_up_pair_list(lines)))))

    # Answer of part 2
    print('Largest magnitude: {}'.format(get_maximum_magnitude(lines)))


if __name__ == "__main__":
    main()
