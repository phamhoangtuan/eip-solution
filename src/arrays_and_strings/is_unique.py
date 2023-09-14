# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique(input_str: str) -> bool:
    """Determine if a string has all unique characters.

    Args:
        input_str: A string to check.

    Returns:
        True if the string has all unique characters, False otherwise.
    """
    tmp_dict = {}

    for char in input_str:
        if char in tmp_dict:
            return False
        tmp_dict[char] = True

    return True


def is_unique_no_additional_data_structure(input_str: str) -> bool:
    """Determine if a string has all unique characters.

    Args:
        input_str: A string to check.

    Returns:
        True if the string has all unique characters, False otherwise.
    """
    sorted_str = sorted(input_str)

    for i in range(len(input_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False

    return True
