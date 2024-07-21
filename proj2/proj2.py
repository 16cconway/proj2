from typing import TextIO
from sys import stderr
from time import time_ns
from proj2.runtime_metric import RuntimeMetric
from proj2.get_input_size import get_input_size
from proj2.get_valid_char import get_valid_char


def convert_prefix_to_postfix_recursive(in_str: str) -> tuple:
    """
    Reads input string as a prefix expression and directly converts it to a
    postfix expression using recursion. Space characters are ignored. Only
    alphabet letters and operators accepted. (num_operators == num_operands - 1)
    :param in_str: input prefix string
    :return: post, in_str, infix: postfix expression, ending state of input
    str, infix expression
    """

    # List of Valid Operators
    valid_ops = ["+", "-", "*", "/", "$", "^"]

    # Read in the first character
    char, in_str = get_valid_char(in_str)

    # Check that the first character is an operator. If not, then the input is
    # not in prefix form. Return -1 in place of char as indicator
    if char not in valid_ops:
        return -1, in_str, -1

    # Check if the character is valid. If not return that character and -2
    # in place of in_str as indicator
    if in_str == -2:
        return char, -2, -2

    # Remove the read in character from the string
    else:
        in_str = in_str[1:]

    # Read in the next character
    temp, in_str = get_valid_char(in_str)

    # Check if no more characters are in the string. If so, return -1 in
    # place of temp character as indicator
    if temp == -1:
        return -1, in_str, -1

    # Check if read in character was valid. If not, return that character and -2
    # in place of in_str as indicator
    elif in_str == -2:
        return temp, -2, -1

    # Check if the read in character is an operator. If so, call the function
    # again
    elif temp in valid_ops:
        char1, in_str, char1_infix = convert_prefix_to_postfix_recursive(in_str)

        # Check if no more characters in string. If so, return -1 in place of
        # temp character as indicator
        if char1 == -1:
            return -1, in_str, -1

        # Check if read in character was valid. If not return that character
        # and -2 in place of in_str as indicator
        elif in_str == -2:
            return char1, -2, -2

    # If else reached, set char1 to temp as first operand operator in char
    else:
        char1 = temp

        # Character 1 for infix notation
        char1_infix = temp

        # Remove char1 from the string
        in_str = in_str[1:]

    # Read in next character
    temp, in_str = get_valid_char(in_str)

    # Check if no more characters in the string. If so, return -1 in
    # place of temp character as indicator
    if temp == -1:
        return -1, in_str, -1

    # Check if read in character was valid. If not, return that character and -2
    # in place of in_str as indicator
    elif in_str == -2:
        return temp, -2, -2

    # Check if the read in character is an operator. If so, call the function
    # again
    elif temp in valid_ops:
        char2, in_str, char2_infix = convert_prefix_to_postfix_recursive(in_str)

        # Check if no more characters in the string. If so, return -1 in
        # place of temp character as indicator
        if char2 == -1:
            return -1, in_str, -1

        # Check if read in character was valid. If not return that character
        # and -2 in place of in_str as indicator
        elif in_str == -2:
            return char2, -2, -2

    # If else reached, set char2 to temp as second operand for operator in char
    else:
        char2 = temp

        # Character 2 for infix notation
        char2_infix = temp

        # Remove char2 from the string
        in_str = in_str[1:]

    # Assemble postfix notation for current operand 1 in char1, operand 2 in
    # char2 and operator in char
    post = char1 + char2 + char

    # Assemble Infix notation of same characters
    infix = "(" + char1_infix + char + char2_infix + ")"

    # Return postfix and current state of input string
    return post, in_str, infix


def starter_func(input_file: TextIO, output_file: TextIO) -> None:

    lines = input_file.readlines()
    line_idx = 0

    # Start time for analyzing computation time of input
    start_time = time_ns()

    # Loop over each line in the input file
    for line in lines:

        # Line Index tracker in case of an error to be outputted to user
        line_idx += 1

        # Check if the line is blank and only contains spaces, tabs, or new
        # line characters. If so, skip this line
        temp = get_valid_char(line)
        if temp[0] == -1:
            continue

        # Call the convert function on the line
        post, end_str, infix = convert_prefix_to_postfix_recursive(line)

        # Write the input expression to the output file accounting for
        # possible new line characters
        if line[len(line)-1] == "\n":
            output_file.write(f"Prefix: {line}")
        else:
            output_file.write(f"Prefix: {line} \n")

        # Check if an invalid character was found during conversion
        if end_str == -2:
            err_msg = (f"Error input line {line_idx}: Invalid character: "
                       f"'{post}'. "
                       f"Only accepts alphabet letters and "
                       f"operators +, -, *, /, $, and ^")

            output_file.write(err_msg + "\n\n")
            print(err_msg, file=stderr)
        else:

            # Check if there still exists characters in the ending string
            next_char, end_str = get_valid_char(end_str)

            # If next_char is not -1, this indicates the string is not empty
            # after algorithm was completed. If post is -1, this indicates
            # the string became empty before the algorithm completed or the
            # first character read was not an operator. All instances mean the
            # input expression is not in a valid prefix notation.
            if next_char != -1 or post == -1:
                err_msg = (f"Error input line {line_idx}: Expression not in "
                           f"prefix notation. Check that there exists "
                           f"one operator each located on the left of two "
                           f"operands. ")

                output_file.write(err_msg + "\n\n")
                print(err_msg, file=stderr)

            # If no errors occur, write the computed postfix expression to
            # the output file
            else:
                output_file.write(f"Postfix: {post}\n")

                # Write the corresponding infix expression to the output file
                output_file.write(f"Infix: {infix[1:-1]}\n\n")

    # End time for analyzing computation time of input
    end_time = time_ns()

    # Write the size and time for the input to the output file
    metric = RuntimeMetric(get_input_size(lines), end_time - start_time)
    output_file.write(f"Input Size: {metric.store_size()}\nRun Time:"
                      f" {metric.get_runtime()}ns\n")
