

from typing import TextIO
# from sys import stderr
# from time import time_ns
# from runtime_metric import RuntimeMetric


def get_valid_char(in_str: str) -> tuple:
    space_chars = ["\n", "\t", " "]

    if not bool(in_str):
        return -1, in_str
    else:
        char = in_str[0]

    while char in space_chars:
        in_str = in_str[1:]
        if not bool(in_str):
            return -1, in_str
        char = in_str[0]

    return char, in_str


def convert_prefix_to_postfix_recursive(in_str: str) -> tuple:
    """
    Reads prefix expressions from an input file and directly writes them as
    postfix expressions to an output file. Empty lines are disregarded. Only
    alphabet letters and operators accepted. (num_operators == num_operands - 1)
    :param
    :param
    :return:
    """

    valid_ops = ["+", "-", "*", "/", "$", "^"]

    char, in_str = get_valid_char(in_str)
    in_str = in_str[1:]

    temp, in_str = get_valid_char(in_str)
    if temp == -1:
        return -1, in_str
    elif temp in valid_ops:
        char1, in_str = convert_prefix_to_postfix_recursive(in_str)
        if char1 == -1:
            return -1, in_str
    else:
        char1, in_str = get_valid_char(in_str)
        in_str = in_str[1:]

    temp, in_str = get_valid_char(in_str)
    if temp == -1:
        return -1, in_str
    elif temp in valid_ops:
        char2, in_str = convert_prefix_to_postfix_recursive(in_str)
        if char2 == -1:
            return -1, in_str
    else:
        char2, in_str = get_valid_char(in_str)
        in_str = in_str[1:]

    post = char1 + char2 + char
    return post, in_str


def starter_func(input_file: TextIO, output_file: TextIO) -> None:
    lines = input_file.readlines()
    line_idx = 0
    for line in lines:
        line_idx += 1

        # Check if line is blank
        temp = get_valid_char(line)
        if temp[0] == -1:
            continue

        post, end_str = convert_prefix_to_postfix_recursive(line)

        # Comment
        if line[len(line)-1] == "\n":
            output_file.write(f"Prefix: {line}")
        else:
            output_file.write(f"Prefix: {line} \n")

        # Comment
        next_char, end_str = get_valid_char(end_str)

        if post == -1:
            output_file.write(f"Error input line {line_idx}: Too many "
                              f"operators \n\n")
        elif next_char != -1:
            output_file.write(f"Error input line {line_idx}: Not enough "
                              "operators \n\n")
        else:
            output_file.write(f"Postfix: {post}\n\n")
