def remove_first_character(str1: str) -> str:
    """
    Removes the first character (0th index) of an input string.
    :param: str1: input string
    :return: str2: str1 without the first character (0th index). Equivalent to str1[1:]
    """
    str2 = ""
    for i in range(1, len(str1)):
        str2 = str2 + str1[i]
    return str2


def remove_first_and_last_character(str1: str) -> str:
    """
    Removes the first and last character (0th and -1st index) of an input string. Equivalent to str1[1:-1]
    :param: str1: input string
    :return: str2: str1 without the first nor last character
    """
    str2 = ""
    for i in range(1, len(str1)-1):
        str2 = str2 + str1[i]
    return str2
