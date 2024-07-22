def get_input_size(lines: list) -> int:
    """
    Gets the size of the input file based on number of characters. All
    characters counted
    :param lines: Lines from input file
    :return: count: the total number of characters in the input file
    """

    valid_ops = ["+", "-", "*", "/", "$", "^"]

    count = 0

    # iterate over all characters within each line of lines and add 1 to count
    for string in lines:
        for char in string:
            count += 1

            # If read character is invalid, continue to next line to mirror how the conversion function would handle
            # invalid character inputs
            if not char.isalpha() or char not in valid_ops:
                continue

    return count
