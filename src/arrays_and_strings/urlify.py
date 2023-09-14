# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end
# to hold the additional characters,
# and that you are given the "true" length of the string.


def urlify(input_str: str, length: int) -> str:
    """Replace all spaces in a string with '%20'.

    Args:
        input_str: A string to replace spaces in.
        length: The "true" length of the string.

    Returns:
        A string with spaces replaced with '%20'.
    """
    space_count = 0
    for i in range(length):
        if input_str[i] == ' ':
            space_count += 1

    new_length = length + space_count * 2
    new_str = [''] * new_length
    for i in range(length - 1, -1, -1):
        if input_str[i] == ' ':
            new_str[new_length - 1] = '0'
            new_str[new_length - 2] = '2'
            new_str[new_length - 3] = '%'
            new_length -= 3
        else:
            new_str[new_length - 1] = input_str[i]
            new_length -= 1

    return ''.join(new_str)
