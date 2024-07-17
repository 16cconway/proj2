from proj1.modify_strings import *
from proj1.stack import Stack
from proj1.get_count import get_count
from typing import TextIO
from sys import stderr
from time import time_ns
from proj1.runtime_metric import RuntimeMetric
from proj1.get_input_size import get_input_size


def convert_prefix_to_postfix(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads prefix expressions from an input file and directly writes them as
    postfix expressions to an output file. Empty lines are disregarded. Only
    alphabet letters and operators accepted. (num_operators == num_operands - 1)
    :param input_file: An opened text file set to read mode
    :param output_file: An opened text file set to write mode
    :return:
    """

    # Start time to analyze computation time of input
    start_time = time_ns()

    lines = input_file.readlines()
    stack1 = Stack()
    valid_ops = ["+",  "-",  "*", "/", "$", "^"]

    for original_prefix_str in lines:

        # Initialize an error flag for characters in string that are not
        # alphabet letters, not in the list of accepted operators,
        # (num_operators != num_operands - 1), or the expression is not in
        # prefix
        err_flag = 0

        # Initialize counts for the number of operators and number of
        # alphabet operands
        ops_count = 0
        alpha_count = 0

        # Retrieve the line index of the input file that is currently being read
        line_idx = lines.index(original_prefix_str) + 1

        # Empty stack if it isn't already
        stack1.empty()

        # Strip whitespace of string expression
        prefix_str = strip_string(original_prefix_str)

        # Checks if line is an empty line after striping \n, \t,
        # and spaces. Empty lines will be disregarded
        if not bool(prefix_str):
            continue

        # Write the prefix expression to the output file
        output_file.write("prefix:  " + original_prefix_str)

        # Reverse the characters in the string expression
        prefix_str = reverse_string(prefix_str)

        for char in prefix_str:

            # If character is an alphabet letter, push it to a stack
            if char.isalpha():
                alpha_count += 1
                stack1.push(char)

            # If character is an operation, pop the top two elements of the
            # stack, form a string of the popped elements and operator,
            # then push that to the stack
            elif char in valid_ops:
                ops_count += 1

                # Checks if an element exists to be popped. If not, the
                # expression has not hit an operator before hitting two
                # operands and the expression is not in prefix
                if stack1.is_empty():

                    # Get the count for number of operands and number of
                    # operators
                    [ops_count, alpha_count] = get_count(prefix_str)
                    err_msg = (f"Input line {line_idx}: The Stack is empty and "
                               f"cannot pop(): encountered an operator before "
                               f"encountering two operands. The Number of "
                               f"Operators must equal the Number of Operands "
                               f"minus 1")

                    count_msg = (f"\nNumber of Operators: {ops_count} "
                                 f"\nNumber of Operands: {alpha_count}\n\n")

                    print(err_msg, file=stderr)
                    output_file.write(err_msg + count_msg)
                    err_flag = 1
                    break
                fir = stack1.pop()

                # Checks if another element exists to be popped. If not, the
                # expression has too many operators
                if stack1.is_empty():

                    # Get the count for number of operands and number of
                    # operators
                    [ops_count, alpha_count] = get_count(prefix_str)
                    err_msg = (f"Input line {line_idx}: The Stack is empty and "
                               f"cannot pop(): too many operators or "
                               f"encountered an operator "
                               f"before encountering two operands. The Number "
                               f"of Operators must equal the Number of "
                               f"Operands minus 1")

                    count_msg = (f"\nNumber of Operators: {ops_count} "
                                 f"\nNumber of Operands: {alpha_count}\n\n")

                    print(err_msg, file=stderr)
                    output_file.write(err_msg + count_msg)
                    err_flag = 1
                    break
                else:
                    sec = stack1.pop()

                    temp = fir + sec + char
                    stack1.push(temp)

            # If else reached, invalid character in the string
            else:
                err_msg = (f"Input line {line_idx}: Invalid character: "
                           f"'{char}'. Only accepts alphabet letters and "
                           f"operators +, -, *, /, $, and ^")
                print(err_msg, file=stderr)
                output_file.write(err_msg + "\n\n")
                err_flag = 1
                stack1.empty()
                break

        # After processing the string, if stack contains more than one element,
        # then there are not enough operators in expression
        if len(stack1.items) > 1:
            err_msg = (f"Input line {line_idx}: Not enough operators. The "
                       f"Number of Operators must equal the Number of "
                       f"Operands minus 1")

            count_msg = (f"\nNumber of Operators: {ops_count} \nNumber of "
                         f"Operands: {alpha_count}\n\n")

            print(err_msg, file=stderr)
            output_file.write(err_msg + count_msg)

        # If no errors occur, write the postfix expression to the output file
        elif not err_flag:
            output_file.write("postfix: " + str(stack1.items[0])+"\n\n")

    # End time for analyzing time of each conversion
    end_time = time_ns()

    # Write the size and time for each string to the output file
    metric = RuntimeMetric(get_input_size(lines), end_time - start_time)
    output_file.write(f"Input Size: {metric.store_size()}\nRun Time:"
                      f" {metric.get_runtime()}ns\n")
