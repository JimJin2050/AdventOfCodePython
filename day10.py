# -*- coding: utf-8 -*-

# read data
with open("data/day10_input.txt") as f:
    data_list = f.readlines()

characters_list = [list(line.strip()) for line in data_list]

BRACKET_SCORE = 3
SQUARE_BRACKET_SCORE = 57
BRACE_SCORE = 1197
ANGLE_BRACKET_SCORE = 25137

LEFT_CHARS = ['(', '[', '{', '<']
RIGHT_CHARS = [')', ']', '}', '>']


# Part 1
def total_syntax_error_score():
    error_count_list = [0] * 4  # error count for bracket, square bracket, brace and angle bracket

    for characters in characters_list:
        left_brace, right_brace = 0, 0
        left_bracket, right_bracket = 0, 0
        left_angle_bracket, right_angle_bracket = 0, 0
        left_square_bracket, right_square_bracket = 0, 0

        left_bracket_indexes = []
        left_square_bracket_indexes = []
        left_brace_indexes = []
        left_angle_bracket_indexes = []

        for index, character in enumerate(characters):
            if character in LEFT_CHARS:
                if character == '(':
                    left_bracket += 1
                    left_bracket_indexes.append(index)
                elif character == '[':
                    left_square_bracket += 1
                    left_square_bracket_indexes.append(index)
                elif character == '{':
                    left_brace += 1
                    left_brace_indexes.append(index)
                elif character == '<':
                    left_angle_bracket += 1
                    left_angle_bracket_indexes.append(index)
            else:
                if character == ')':
                    if left_bracket > right_bracket:
                        if not characters_have_been_paired(characters, left_bracket_indexes, index + 1):
                            error_count_list[0] += 1
                            break
                        else:
                            right_bracket += 1
                    else:
                        error_count_list[0] += 1
                        break
                elif character == ']':
                    if left_square_bracket > right_square_bracket:
                        if not characters_have_been_paired(characters, left_square_bracket_indexes, index + 1):
                            error_count_list[1] += 1
                            break
                        else:
                            right_square_bracket += 1
                    else:
                        error_count_list[1] += 1
                        break
                elif character == '}':
                    if left_brace > right_brace:
                        if not characters_have_been_paired(characters, left_brace_indexes, index + 1):
                            error_count_list[2] += 1
                            break
                        else:
                            right_brace += 1
                    else:
                        error_count_list[2] += 1
                        break
                elif character == '>':
                    if left_angle_bracket > right_angle_bracket:
                        if not characters_have_been_paired(characters, left_angle_bracket_indexes, index + 1):
                            error_count_list[3] += 1
                            break
                        else:
                            right_angle_bracket += 1
                    else:
                        error_count_list[3] += 1
                        break
    return sum([
        BRACKET_SCORE * error_count_list[0], SQUARE_BRACKET_SCORE * error_count_list[1],
        BRACE_SCORE * error_count_list[2], ANGLE_BRACKET_SCORE * error_count_list[3]
    ])


def characters_have_been_paired(characters, left_indexes, end_index):
    been_paired = False
    for index in left_indexes:
        char_list = characters[index: end_index]
        been_paired = been_paired or all([
            char_list.count('(') == char_list.count(')'),
            char_list.count('[') == char_list.count(']'),
            char_list.count('{') == char_list.count('}'),
            char_list.count('<') == char_list.count('>')
        ])

    return been_paired


# part 2
def multiply_three_largest_basins():
    left_brace, right_brace = [], []
    left_brackets, right_brackets = [], []
    left_angle_bracket, right_angle_bracket = [], []
    left_square_bracket, right_square_bracket = [], []



if __name__ == "__main__":
    score = total_syntax_error_score()
    print(score)
