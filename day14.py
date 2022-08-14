# -*- coding: utf-8 -*-
"""
key tips:
1. Only related to the quantity of chars, instead of the sequence;
2. The pair would not can be found in rules if it is not found in rules at first time;
3. A pair is composed of 2 chars: char_1 and char_2. Only two pairs would be generated after inserted
   a new char: (char_1, char_new), (char_new, char_2);
4. New pair not always can be found in rules;
5. Same pair would appear multiple times in the process;
"""


def process_steps(template, rule_info_dict, steps):
    pair_counter_dict = get_counter_dict(get_possible_combination(template))
    chars_counter_dict = get_counter_dict(list(template))

    for n in range(steps):
        pair_counter_dict = process_one_step(pair_counter_dict, rule_info_dict, chars_counter_dict)

    return chars_counter_dict


def process_one_step(pair_counter_dict, rule_info_dict, chars_counter_dict):
    combination_dict = {}
    for pair, count in pair_counter_dict.items():
        element = rule_info_dict[pair]
        combination_dict[pair[0] + element] = combination_dict.get(pair[0] + element, 0) + count
        combination_dict[element + pair[1]] = combination_dict.get(element + pair[1], 0) + count
        chars_counter_dict[element] = chars_counter_dict.get(element, 0) + count

    return combination_dict


def get_possible_combination(template):
    return [char1 + char2 for char1, char2 in zip(template, template[1:])]


def get_counter_dict(key_list):
    counter_dict = {}
    for key in key_list:
        if counter_dict.get(key, None):
            counter_dict[key] += 1
        else:
            counter_dict[key] = 1

    return counter_dict


# def one_polymer_step(template_list, rule_dict):
#     new_template_list = [template_list[0]]
#     for i in range(len(template_list) - 1):
#         pair = template_list[i: i+2]
#         insert_element = rule_dict.get("".join(pair), None)
#         if insert_element:
#             new_template_list.append(insert_element)
#             new_template_list.append(pair[1])
#         else:
#             new_template_list.append(pair[1])
#
#     return new_template_list


if __name__ == "__main__":
    # read data
    with open("data/day14_input.txt") as f:
        data_list = f.readlines()

    # parse data
    polymer_template, rule_dict = None, {}
    for line in data_list:
        if line.strip():
            if "->" in line:
                key, value = line.strip().split("->")
                rule_dict[key.strip()] = value.strip()
            else:
                polymer_template = line.strip()

    # part 1
    print("Answer of part 1:")
    chars_dict = process_steps(polymer_template, rule_dict, 10)
    print(max(chars_dict.values()) - min(chars_dict.values()))

    # part 2
    print("Answer of part 2:")
    chars_dict = process_steps(polymer_template, rule_dict, 40)
    print(max(chars_dict.values()) - min(chars_dict.values()))

