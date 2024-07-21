def get_valid_char(in_str: str) -> tuple:
    """
    Reads the next character of input string until a character that is not a
    tab ("\t"), space (" "), nor a  ("\n"). Valid Characters are alphabet
    letters and operators +, -, *, /, $, and ^
    @param in_str: input string
    @return: char, in_str: tuple of the next character and the updated
    in_str. Returns character for char and -2 for in_str if next character is
    invalid
    """

    # List of Valid Operators
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
