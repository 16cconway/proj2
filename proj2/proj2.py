

from typing import TextIO
from sys import stderr
from time import time_ns
from runtime_metric import RuntimeMetric


def get_valid_char(in_str: str) -> tuple:
    space_chars = ["\n", "\t", " "]

    char = in_str[0]
    while char in space_chars:
        in_str = in_str[1:]
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


with open("../resources/input/RequiredInput.txt") as input_file:
    lines = input_file.readlines()

inp = lines[0]

res, end_str = convert_prefix_to_postfix_recursive(inp)
print(inp)
print(res)


def helper():
    for line in lines:
        if line[len(line)-1] == "\n":
            write(f"prefix: {line}")
        else:
            write(f"prefix: {line} \n")
