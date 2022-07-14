# -*- coding: utf-8 -*-


# Part 1
def calculate_at_least_two_lines_overlapped_for_horizontal_vertical(segments, n):
    count = 0
    marks = [[0] * n for _ in range(n)]
    flags = [[0] * n for _ in range(n)]

    for segment in segments:
        start_point, end_point = segment
        start_x, start_y, end_x, end_y = start_point + end_point

        if start_x == end_x:
            for idx in range(min(start_y, end_y), max(start_y, end_y) + 1):
                marks[start_x][idx] += 1
                if flags[start_x][idx] == 0 and marks[start_x][idx] >= 2:
                    count += 1
                    flags[start_x][idx] = 1
        elif start_y == end_y:
            for idx in range(min(start_x, end_x), max(start_x, end_x) + 1):
                marks[idx][end_y] += 1
                if flags[idx][end_y] == 0 and marks[idx][end_y] >= 2:
                    count += 1
                    flags[idx][end_y] = 1
        else:
            print("Valid point: ", start_x, start_y, end_x, end_y)

    return count


# part 2
def calculate_at_least_two_lines_overlapped_for_horizontal_vertical_diagonal(segments, n):
    marks = [[0] * n for _ in range(n)]

    for segment in segments:
        start_point, end_point = segment
        start_x, start_y, end_x, end_y = start_point + end_point

        if start_x == end_x:
            for idx in range(min(start_y, end_y), max(start_y, end_y) + 1):
                marks[start_x][idx] += 1
        elif start_y == end_y:
            for idx in range(min(start_x, end_x), max(start_x, end_x) + 1):
                marks[idx][end_y] += 1
        else:
            if abs(start_x - end_x) == abs(start_y - end_y):
                x1, y1, x2, y2 = start_x, start_y, end_x, end_y
                while x1 != x2 and y1 != y2:
                    marks[x1][y1] += 1
                    x1 = x1 + 1 if x1 < x2 else x1 - 1
                    y1 = y1 + 1 if y1 < y2 else y1 - 1
                marks[x2][y2] += 1
            else:
                pass

    count = 0
    for row in range(n):
        for col in range(n):
            if marks[row][col] >= 2:
                count += 1

    return count


if __name__ == "__main__":
    # read data
    with open("data/day5_input.txt") as f:
        data_list = f.readlines()

    # parse data
    segments = [
        [
            [
                int(line.strip().split("->")[0].strip().split(",")[0]),
                int(line.strip().split("->")[0].strip().split(",")[1])],
            [
                int(line.strip().split("->")[1].strip().split(",")[0]),
                int(line.strip().split("->")[1].strip().split(",")[1])]
        ] for line in data_list
    ]

    # calculation
    print(calculate_at_least_two_lines_overlapped_for_horizontal_vertical(segments, 999))
    print(calculate_at_least_two_lines_overlapped_for_horizontal_vertical_diagonal(segments, 999))
