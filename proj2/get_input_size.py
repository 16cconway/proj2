def get_input_size(lines: list) -> int:
    """
    Gets the size of the input file based on number of characters
    :param lines: Lines from input file
    :return: count: the total number of characters in the input file
    """
    count = 0

    # iterate over all characters within each line of lines and add 1 to count
    for string in lines:
        for char in string:
            count += 1

    return count
