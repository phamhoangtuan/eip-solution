# Given two strings, write a method to decide if one is a permutation of the other.


def check_permutation(str1: str, str2: str) -> bool:
    """Check if one string is a permutation of the other.

    Args:
        str1: A string to check.
        str2: A string to check.

    Returns:
        True if one string is a permutation of the other, False otherwise.
    """
    if len(str1) != len(str2):
        return False

    tmp_dict: dict = {}
    for char in str1:
        if char in tmp_dict:
            tmp_dict[char] += 1
        else:
            tmp_dict[char] = 1

    for char in str2:
        if char in tmp_dict:
            tmp_dict[char] -= 1
            if tmp_dict[char] < 0:
                return False
        else:
            return False

    return True
