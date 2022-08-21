# -*- coding: utf-8 -*-
import numpy as np

HEX_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

OPS_MAP = {
    0: lambda ops: sum(ops),
    1: lambda ops: np.prod(ops),
    2: lambda ops: min(ops),
    3: lambda ops: max(ops),
    5: lambda ops: int(ops[0] > ops[1]),
    6: lambda ops: int(ops[0] < ops[1]),
    7: lambda ops: int(ops[0] == ops[1]),
}


def read_packet(bin_str: str) -> (int, int, int):
    return int(bin_str[:3], 2), int(bin_str[3:6], 2), 6


def to_binary(hex_str: str) -> str:
    binary_str = ""
    for c in hex_str:
        binary_str += HEX_MAP.get(c.upper())

    return binary_str


def parse_literal_packet(bin_str: str) -> (int, int):
    _, _, index = read_packet(bin_str)

    index, parsed_literal = 0, ""

    while bin_str[index] == "1":
        five_bits = bin_str[index: 5 + index]
        index += 5
        parsed_literal += five_bits[1:]

    last_five_bits = bin_str[index: 5 + index]
    parsed_literal += last_five_bits[1:]
    index += 5

    return int(parsed_literal, 2), index


def parse_operator_packet(bin_str: str) -> (int, int, str):
    index = 0
    length_type_id = int(bin_str[index], 2)
    index += 1

    if length_type_id == 0:
        return length_type_id, index + 15, bin_str[index: index + 15]
    else:
        return length_type_id, index + 11, bin_str[index: index + 11]


def add_up_version_number(bits_str: str) -> int:
    version_amount, index, length = 0, 0, len(bits_str)

    while index < length and int(bits_str[index:], 2) > 0:
        version, type_id, index_delta = read_packet(bits_str[index:])
        version_amount += version
        index += index_delta

        if type_id == 4:
            _, index_delta = parse_literal_packet(bits_str[index:])
            index += index_delta
        else:
            _, index_delta, _ = parse_operator_packet(bits_str[index:])
            index += index_delta

    return version_amount


def evaluate_packet(bits_str: str) -> int:
    index = 0
    _, type_id, index_delta = read_packet(bits_str[index:])
    index += index_delta

    stack = []
    if type_id == 4:                                      # a literal packet
        return parse_literal_packet(bits_str[index:])[0]
    else:                                                 # an operator packet
        index += 1
        if bits_str[index] == '0':                        # an operator packet with fixed number of bits
            index += 15
            stack.append([type_id, index + int(bits_str[index - 15: index], 2), -1, []])
        else:
            index += 11                                   # an operator packet with fixed number of sub-packets
            stack.append([type_id, -1, int(bits_str[index - 11: index], 2), []])

    operand = None                                                 # an operand, also can be a calculation result
    while stack:
        operator_data = stack[-1]                                  # get last element
        if operand is not None:                                    # add operand
            operator_data[3].append(operand)

        if index == operator_data[1] or operator_data[2] == 0:     # already reach the number of bits or sub-packets
            operand = OPS_MAP[operator_data[0]](operator_data[3])
            stack.pop()                                            # remove from stack
            continue

        if operator_data[2] >= 0:                                  # count the number of sub-packets
            operator_data[2] -= 1

        index += 3
        t_id = int(bits_str[index: index + 3], 2)
        index += 3
        if t_id == 4:
            operand, delta = parse_literal_packet(bits_str[index:])
            index += delta
        else:
            operand = None                                         # reset before start to parse an operator packet
            index += 1
            if bits_str[index - 1] == '0':
                index += 15
                stack.append([t_id, index + int(bits_str[index - 15: index], 2), -1, []])
            else:
                index += 11
                stack.append([t_id, -1, int(bits_str[index - 11: index], 2), []])

    return operand


if __name__ == "__main__":
    # read data
    with open("data/day16_input.txt") as f:
        data_list = f.readlines()

    # parse data
    packets_str = to_binary(data_list[0].strip())
    print(len(packets_str))

    # part 1
    print("Answer of part 1:")
    print(add_up_version_number(packets_str))

    # part 2
    print("Answer of part 2:")
    print(evaluate_packet(packets_str))

