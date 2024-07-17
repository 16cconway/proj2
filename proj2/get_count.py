def get_count(str1: str) -> list:
    """
    Counts the number of operators ("+", "-", "*", "/", "$", "^") and number
    of alphabet letter operands. All other characters are ignored
    :param str1: Input string
    :return: list consisting of number of operators and number of operands
    """
    valid_ops = ["+", "-", "*", "/", "$", "^"]
    num_ops = 0
    num_alpha = 0

    # Loop through the string and add 1 to num_alpha if encounter an alphabet
    # letter or add 1 to num_ops if encounter an operator
    for char in str1:
        if char.isalpha():
            num_alpha += 1
        elif char in valid_ops:
            num_ops += 1

        # Continue if any other character is encountered
        else:
            continue
    return [num_ops, num_alpha]
