

from typing import TextIO
from sys import stderr
# from time import time_ns
# from runtime_metric import RuntimeMetric


def get_valid_char(in_str: str) -> tuple:
    """
    Reads the next character of input string until a character that is not a
    tab ("\t"), space (" "), nor a  ("\n")
    @param in_str: input string
    @return: char, in_str: tuple of the next character and the updated in_str
    """

    # Valid Operators
    valid_ops = ["+", "-", "*", "/", "$", "^"]

    # Space characters that are to be skipped over
    space_chars = ["\n", "\t", " "]

    # Check that the input string is not already empty
    if not bool(in_str):
        return -1, in_str
    else:
        char = in_str[0]

    # Continue looping through and deleting characters from the input string
    # until a non-space character is found. -1 indicator used for empty string
    while char in space_chars:
        in_str = in_str[1:]

        # After each removal of a character from the input string, check if
        # the string is empty. -1 indicator used for empty string
        if not bool(in_str):
            return -1, in_str
        char = in_str[0]

    # Check that the character is a valid alphabet letter operand or a
    # valid operator
    if not char.isalpha() and char not in valid_ops:
        return char, -2

    return char, in_str


def convert_prefix_to_postfix_recursive(in_str: str) -> tuple:
    """
    Reads input string as a prefix expression and directly converts it to a
    postfix expression using recursion. Space characters are ignored. Only
    alphabet letters and operators accepted. (num_operators == num_operands - 1)
    :param in_str: input prefix string
    :return: post, in_str: postfix expression, ending state of input str
    """

    valid_ops = ["+", "-", "*", "/", "$", "^"]

    char, in_str = get_valid_char(in_str)

    # C
    if in_str == -2:
        return char, -2

    # C
    in_str = in_str[1:]

    temp, in_str = get_valid_char(in_str)
    if temp == -1:
        return -1, in_str
    elif in_str == -2:
        return temp, -2
    elif temp in valid_ops:
        char1, in_str = convert_prefix_to_postfix_recursive(in_str)

        # Check if string in empty after last
        if char1 == -1:
            return -1, in_str

        # Check if invalid character was found
        elif in_str == -2:
            return char1, -2
    else:
        char1, in_str = get_valid_char(in_str)

        # Check if invalid character was found
        if in_str == -2:
            return char1, -2

        # If character valid, remove it from string
        in_str = in_str[1:]

    # C
    temp, in_str = get_valid_char(in_str)
    if temp == -1:
        return -1, in_str
    elif in_str == -2:
        return temp, -2
    elif temp in valid_ops:
        char2, in_str = convert_prefix_to_postfix_recursive(in_str)

        # Check if string is empty after last
        if char2 == -1:
            return -1, in_str

        # Check if invalid character was found
        elif in_str == -2:
            return char2, -2

    else:
        char2, in_str = get_valid_char(in_str)

        # Check if invalid character was found
        if in_str == -2:
            return char2, -2

        # If character valid, remove it from string
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

        if end_str == -2:
            err_msg = (f"Input line {line_idx}: Invalid character: '{post}'. "
                       f"Only accepts alphabet letters and "
                       f"operators +, -, *, /, $, and ^")

            output_file.write(err_msg + "\n\n")
            print(err_msg, file=stderr)
        else:

            # Comment
            next_char, end_str = get_valid_char(end_str)

            if post == -1:
                err_msg = f"Error input line {line_idx}: Too many operators"

                output_file.write(err_msg + "\n\n")
                print(err_msg, file=stderr)
            elif next_char != -1:
                err_msg = (f"Error input line {line_idx}: Expression not in prefix "
                           f"notation. Check that operators are left of two "
                           f"operands ")

                output_file.write(err_msg + "\n\n")
                print(err_msg, file=stderr)

            else:
                output_file.write(f"Postfix: {post}\n\n")
