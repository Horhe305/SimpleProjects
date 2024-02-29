"""Generating random password module."""
from random import choice


def get_all_characters_in_range(start_unicode: int, end_unicode: int) -> list[str]:
    """
    Get a list of all characters in provided unicode ranges.
    :param start_unicode: Start of the unicode range.
    :param end_unicode: End of the unicode range.
    :return: List of characters in the range.
    """
    return [chr(character) for character in range(start_unicode, end_unicode + 1)]


def generate_random_password(length: int = 8, start_unicode: int = 33, end_unicode: int = 127) -> str:
    """
    Generate a random password.
    :param length: Length of the password.
    :param start_unicode: Start of the unicode chars range for the password.
    :param end_unicode: End of the unicode chars range for the password.
    :return: Random password.
    """
    available_chars = get_all_characters_in_range(start_unicode, end_unicode)
    password = ''.join([choice(available_chars) for _ in range(length)])
    return password


if __name__ == '__main__':
    quantity = int(input('How many passwords do you want? '))
    quality = int(input('How many characters you want in your password(s)? '))
    while quantity:
        print(generate_random_password(quality))
        quantity -= 1
