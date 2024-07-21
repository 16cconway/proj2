from proj2.get_valid_char import get_valid_char


def prefix_to_infix_recursive(in_str: str) -> tuple:

    # List of Valid Operators
    valid_ops = ["+", "-", "*", "/", "$", "^"]

    # Read in the first character
    char, in_str = get_valid_char(in_str)

    # Remove the read in character from the string
    in_str = in_str[1:]

    # Read in the next character
    temp, in_str = get_valid_char(in_str)

    # Check if the read in character is an operator. If so, call the function
    # again
    if temp in valid_ops:
        char1, in_str = prefix_to_infix_recursive(in_str)

    # If else reached, set char1 to temp as first operand operator in char
    else:
        char1 = temp

        # Remove char1 from the string
        in_str = in_str[1:]

    # Read in next character
    temp, in_str = get_valid_char(in_str)

    # Check if the read in character is an operator. If so, call the function
    # again
    if temp in valid_ops:
        char2, in_str = prefix_to_infix_recursive(in_str)

    # If else reached, set char2 to temp as second operand for operator in char
    else:
        char2 = temp

        # Remove char2 from the string
        in_str = in_str[1:]

    # Assemble postfix notation for current operand 1 in char1, operand 2 in
    # char2 and operator in char
    infix = "(" + char1 + char + char2 + ")"
    return infix, in_str



