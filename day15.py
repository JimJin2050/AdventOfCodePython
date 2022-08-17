# -*- coding: utf-8 -*-
import heapq


def lowest_risk_path(risk_matrix):
    rows, cols = len(risk_matrix), len(risk_matrix[0])
    is_visited_list, heap_list = [], []

    heap_list.append([0, [0, 0]])  # [0, 0] means the top-left point, and init risk is 0.
    is_visited_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    while heap_list:
        # Generate a heap which is a binary tree for every parent less than or equal to its children.
        heapq.heapify(heap_list)
        # Get lowest risk from existing heap
        lowest_risk, (col, row) = heapq.heappop(heap_list)

        if col + 1 == cols and row + 1 == rows:
            return lowest_risk
        else:
            for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                move_to_col, move_to_row = col + move[0], row + move[1]

                if 0 <= move_to_row < rows and 0 <= move_to_col < cols:
                    if is_visited_matrix[move_to_col][move_to_row] == 0:
                        is_visited_matrix[move_to_col][move_to_row] = 1  # mark it as visited

                        risk_count = risk_matrix[move_to_col][move_to_row] + lowest_risk

                        if [risk_count, [move_to_col, move_to_row]] not in heap_list:
                            heap_list.append([risk_count, [move_to_col, move_to_row]])


def generate_five_times_matrix(risk_matrix):
    large_matrix = []
    rows, cols = len(risk_matrix), len(risk_matrix[0])
    for j in range(5):
        for row in range(rows):
            row_list = risk_matrix[row]
            temp_list = []
            for i in range(5):
                temp_list += [
                    9 if (row_list[col] + i + j) % 9 == 0 else (row_list[col] + i + j) % 9
                    for col in range(cols)
                ]
            large_matrix.append(temp_list)

    return large_matrix


if __name__ == "__main__":
    # read data
    with open("data/day15_input.txt") as f:
        data_list = f.readlines()

    # parse data
    risk_map = [list(map(int, list(line.strip()))) for line in data_list]

    # part 1
    print("Answer of part 1:")
    print(lowest_risk_path(risk_map))

    # part 2
    print("Answer of part 2:")
    large_map = generate_five_times_matrix(risk_map)
    print(lowest_risk_path(large_map))
