# -*- coding: utf-8 -*-
import math

# read data
with open("data/day9_input.txt") as f:
    data_list = f.readlines()

heightmap = [list(map(int, line.strip())) for line in data_list]


# Part 1
def sum_of_risk_level():
    low_points = find_low_points(heightmap)
    return sum([heightmap[point_data[0]][point_data[1]] + 1 for point_data in low_points])


# part 2
def multiply_three_largest_basins():
    basin_sizes, a_basin = list(), set()
    low_points = find_low_points(heightmap)
    for low_point in low_points:
        a_basin.add(low_point)
        row, col = low_point
        if row + 1 < len(heightmap):
            search_basin_points(row + 1, col, a_basin)
        if row - 1 >= 0:
            search_basin_points(row - 1, col, a_basin)
        if col + 1 < len(heightmap[0]):
            search_basin_points(row, col + 1, a_basin)
        if col - 1 >= 0:
            search_basin_points(row, col - 1, a_basin)

        basin_sizes.append(len(a_basin))
        a_basin.clear()

    return math.prod(sorted(basin_sizes, reverse=True)[:3])


def find_low_points(heightmap_matrix):
    low_points = []
    rows, cols = len(heightmap_matrix), len(heightmap_matrix[0])
    for row in range(rows):
        for col in range(cols):
            height = heightmap_matrix[row][col]
            if height != '9':
                if row - 1 >= 0:
                    if heightmap_matrix[row - 1][col] <= height:
                        continue
                if row + 1 < rows:
                    if heightmap_matrix[row + 1][col] <= height:
                        continue
                if col - 1 >= 0:
                    if heightmap_matrix[row][col - 1] <= height:
                        continue
                if col + 1 < cols:
                    if heightmap_matrix[row][col + 1] <= height:
                        continue

                low_points.append((row, col))

    return low_points


def search_basin_points(row, col, points_set):
    if heightmap[row][col] != 9:
        if (row, col) not in points_set:
            points_set.add((row, col))
            if row + 1 < len(heightmap):
                search_basin_points(row + 1, col, points_set)
            if row - 1 >= 0:
                search_basin_points(row - 1, col, points_set)
            if col + 1 < len(heightmap[0]):
                search_basin_points(row, col + 1, points_set)
            if col - 1 >= 0:
                search_basin_points(row, col - 1, points_set)


if __name__ == "__main__":
    print(sum_of_risk_level())
    print(multiply_three_largest_basins())
