# -*- coding: utf-8 -*-

# Part 1
def calculate_win_first_final_score(draw_numbers, boards, number_index_maps, boards_marks):
    """
    :param draw_numbers: The numbers would be drawn on each board
    :param boards: The list record all boards of game
    :param number_index_maps: The dict which record the index of each element in board
    :param boards_marks: 2-d array which record if the element has been marked
    :return: final score
    """
    boards_total, board_rows, board_cols = len(boards), len(boards[0]), len(boards[0][0])

    for draw_num in draw_numbers:
        for idx, cur_board in enumerate(boards):
            cur_marks, cur_number_index_map = boards_marks[idx], number_index_maps[idx]
            if int(draw_num) in cur_number_index_map:
                target_row, target_col = cur_number_index_map.get(int(draw_num))
                cur_marks[target_row][target_col] = 1

                if any([sum([cur_marks[row][target_col] for row in range(board_rows)]) == board_rows,
                        sum([cur_marks[target_row][col] for col in range(board_cols)]) == board_cols]):
                    sum_of_unmarked = 0
                    for row in range(board_rows):
                        for col in range(board_cols):
                            if not cur_marks[row][col]:
                                sum_of_unmarked += cur_board[row][col]

                    return int(draw_num) * sum_of_unmarked
    else:
        return 0


# part 2
def calculate_win_last_final_score(draw_numbers, boards, number_index_maps, boards_marks):
    boards_total, board_rows, board_cols = len(boards), len(boards[0]), len(boards[0][0])

    won_boards = [0] * boards_total
    for draw_num in draw_numbers:
        for idx, cur_board in enumerate(boards):
            cur_marks, cur_number_index_map = boards_marks[idx], number_index_maps[idx]
            if int(draw_num) in cur_number_index_map:
                target_row, target_col = cur_number_index_map.get(int(draw_num))
                cur_marks[target_row][target_col] = 1
                if any([sum([cur_marks[row][target_col] for row in range(board_rows)]) == board_rows,
                        sum([cur_marks[target_row][col] for col in range(board_cols)]) == board_cols]):
                    won_boards[idx] = 1

                    if sum(won_boards) == boards_total:
                        sum_of_unmarked = 0
                        for row in range(board_rows):
                            for col in range(board_cols):
                                if not cur_marks[row][col]:
                                    sum_of_unmarked += cur_board[row][col]

                        return int(draw_num) * sum_of_unmarked
    else:
        return 0


if __name__ == "__main__":
    # read data
    with open("data/day4_input.txt") as f:
        data_list = f.readlines()

    # parse data
    draw_numbers, boards, temp_board = data_list[0].strip().split(","), [], []
    for idx in range(1, len(data_list)):
        if len(data_list[idx].strip()) != 0:
            temp_board.append([int(c) for c in data_list[idx].strip().split()])
        else:
            if temp_board:
                boards.append(temp_board)
            temp_board = []
    boards.append(temp_board)

    # init data
    number_index_maps, boards_marks = [], []
    board_rows, board_cols = len(boards[0]), len(boards[0][0])
    for board in boards:
        indexes = [[row, col] for col in range(board_cols) for row in range(board_rows)]
        number_index_maps.append(dict(zip(sum(board, []), indexes)))
        boards_marks.append([[0] * board_cols for _ in range(board_rows)])

    # calculate final score
    print(calculate_win_first_final_score(
        draw_numbers,
        boards,
        number_index_maps,
        boards_marks
    ))
    print(calculate_win_last_final_score(
        draw_numbers, boards,
        number_index_maps,
        boards_marks
    ))
