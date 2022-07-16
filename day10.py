# -*- coding: utf-8 -*-
from queue import LifoQueue

# read data
with open("data/day10_input.txt") as f:
    data_list = f.readlines()

characters_list = [list(line.strip()) for line in data_list]

BRACKET_SCORE = 3
SQUARE_BRACKET_SCORE = 57
BRACE_SCORE = 1197
ANGLE_BRACKET_SCORE = 25137

CHAR_PAIR = {'(': ')', '[': ']', '{': '}', '<': '>'}


# Part 1
def calculate_total_syntax_error_score():
    error_count_list, _ = get_error_count_list_and_incomplete_chars()

    return sum([
        BRACKET_SCORE * error_count_list[0], SQUARE_BRACKET_SCORE * error_count_list[1],
        BRACE_SCORE * error_count_list[2], ANGLE_BRACKET_SCORE * error_count_list[3]
    ])


# part 2
def calculate_middle_score():
    _, incomplete_chars = get_error_count_list_and_incomplete_chars()
    supplementary_chars = [[] for _ in range(len(incomplete_chars))]

    for index, characters in enumerate(incomplete_chars):
        chars_stack = LifoQueue()
        end = len(characters) - 1

        while end >= 0:
            if characters[end] in ['(', '[', '{', '<']:
                if chars_stack.empty():
                    supplementary_chars[index].append(CHAR_PAIR.get(characters[end]))
                else:
                    top_element = chars_stack.get()
                    if not CHAR_PAIR.get(characters[end]) == top_element:
                        supplementary_chars[index].append(CHAR_PAIR.get(characters[end]))
                        chars_stack.put(top_element)
            else:
                chars_stack.put(characters[end])
            end -= 1

    middle_score = calculate_supplementary_score(supplementary_chars)
    return middle_score


def get_error_count_list_and_incomplete_chars():
    incomplete_chars = []
    error_count_list = [0] * 4  # error count for bracket, square bracket, brace and angle bracket

    for characters in characters_list:
        # record the index of left bracket, left square bracket, left brace and left angle bracket
        left_characters = [[] for _ in range(4)]
        # record the index of right bracket, right square bracket, right brace and right angle bracket
        right_characters = [[] for _ in range(4)]

        for index, character in enumerate(characters):
            if character in ['(', '[', '{', '<']:
                if character == '(':
                    left_characters[0].append(index)
                elif character == '[':
                    left_characters[1].append(index)
                elif character == '{':
                    left_characters[2].append(index)
                elif character == '<':
                    left_characters[3].append(index)
            else:
                if character == ')':
                    if len(left_characters[0]) > len(right_characters[0]):
                        if not characters_have_been_paired(characters, left_characters[0], index + 1):
                            error_count_list[0] += 1
                            break
                        else:
                            right_characters[0].append(index)
                    else:
                        error_count_list[0] += 1
                        break
                elif character == ']':
                    if len(left_characters[1]) > len(right_characters[1]):
                        if not characters_have_been_paired(characters, left_characters[1], index + 1):
                            error_count_list[1] += 1
                            break
                        else:
                            right_characters[1].append(index)
                    else:
                        error_count_list[1] += 1
                        break
                elif character == '}':
                    if len(left_characters[2]) > len(right_characters[2]):
                        if not characters_have_been_paired(characters, left_characters[2], index + 1):
                            error_count_list[2] += 1
                            break
                        else:
                            right_characters[2].append(index)
                    else:
                        error_count_list[2] += 1
                        break
                elif character == '>':
                    if len(left_characters[3]) > len(right_characters[3]):
                        if not characters_have_been_paired(characters, left_characters[3], index + 1):
                            error_count_list[3] += 1
                            break
                        else:
                            right_characters[3].append(index)
                    else:
                        error_count_list[3] += 1
                        break

            if index == len(characters) - 1:
                incomplete_chars.append(characters)

    return error_count_list, incomplete_chars


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


def calculate_supplementary_score(supplementary_chars):
    score_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    score_list = [0] * len(supplementary_chars)

    for index, chars in enumerate(supplementary_chars):
        for char in chars:
            score_list[index] = score_list[index] * 5 + score_dict[char]

    return sorted(score_list)[len(score_list)//2]


if __name__ == "__main__":
    print(calculate_total_syntax_error_score())
    print(calculate_middle_score())
