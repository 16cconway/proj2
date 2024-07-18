

from typing import TextIO
# from sys import stderr
# from time import time_ns
# from runtime_metric import RuntimeMetric


def get_valid_char(in_str: str) -> tuple:
    space_chars = ["\n", "\t", " "]

    char = in_str[0]
    while char in space_chars:
        in_str = in_str[1:]
        if not bool(in_str):
            return 0, in_str
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
    if temp in valid_ops:
        char1, in_str = convert_prefix_to_postfix_recursive(in_str)

    else:
        char1, in_str = get_valid_char(in_str)
        in_str = in_str[1:]

    temp, in_str = get_valid_char(in_str)
    if temp in valid_ops:
        char2, in_str = convert_prefix_to_postfix_recursive(in_str)
    else:
        char2, in_str = get_valid_char(in_str)
        in_str = in_str[1:]

    post = char1 + char2 + char
    return post, in_str


def starter_func(input_file: TextIO, output_file: TextIO) -> None:
    lines = input_file.readlines()
    for line in lines:
        post, in_str = convert_prefix_to_postfix_recursive(line)

        if line[len(line)-1] == "\n":
            output_file.write(f"Prefix: {line}")
        else:
            output_file.write(f"Prefix: {line} \n")

        output_file.write(f"Postfix: {post}\n\n")
