# -*- coding: utf-8 -*-

DIGIT_1478_LEN_LIST = [2, 4, 3, 7]  # The length of digit 1, 4, 7, 8 in seven segment


# Part 1
def times_of_1478_appear(outputs_list):  # Part 1
    return sum(sum([[1 if len(digit) in DIGIT_1478_LEN_LIST else 0 for digit in ot] for ot in outputs_list], []))


# part 2
def sum_of_output_base_on_fix_configuration(outputs_list, signals_list):
    total = 0
    for index, output in enumerate(outputs_list):
        seven_segment_map = get_seven_segment_mapping(signals_list[index])
        digit_lenth = len(output)
        for idx, digit in enumerate(output):
            digit_map_key = "".join(sorted(list(digit)))
            total += seven_segment_map.get(digit_map_key) * 10 ** (digit_lenth - idx - 1)

    return total


def get_seven_segment_mapping(signal_pattens):
    digits, segments = [""] * 10, ['0'] * 7
    signals_length_is_5, signals_length_is_6 = [], []

    for signal in signal_pattens:
        key = "".join(sorted(list(signal)))
        if len(signal) == 2:
            digits[1] = key
        elif len(signal) == 3:
            digits[7] = key
        elif len(signal) == 4:
            digits[4] = key
        elif len(signal) == 5:
            signals_length_is_5.append(key)
        elif len(signal) == 6:
            signals_length_is_6.append(key)
        elif len(signal) == 7:
            digits[8] = key
        else:
            raise ValueError("Invalid signal pattern of seven-segments")

    for signal in signals_length_is_6:
        intersection = set(signal).intersection(set(digits[1]))
        if len(intersection) == 1:
            digits[6] = signal
            segments[2] = set(digits[1]).difference(intersection).pop()
        else:
            diff = set(digits[4]).difference(set(signal))
            if len(diff) == 0:
                digits[9] = signal
                segments[4] = set(digits[8]).difference(set(signal)).pop()
            else:
                digits[0] = signal

    for signal in signals_length_is_5:
        if segments[4] in signal:
            digits[2] = signal
        elif segments[2] in signal:
            digits[3] = signal
        else:
            digits[5] = signal

    return dict(zip(digits, [idx for idx in range(len(digits))]))


if __name__ == "__main__":
    # read data
    with open("data/day8_input.txt") as f:
        data_list = f.readlines()

    # parse data
    input_list, output_list = [], []
    for line in data_list:
        signals, outputs = line.split("|")
        input_list.append(signals.split())
        output_list.append(outputs.split())

    # process
    print(times_of_1478_appear(output_list))
    print(sum_of_output_base_on_fix_configuration(output_list, input_list))
