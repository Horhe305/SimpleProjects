"""Generating random password module."""

from random import choice


class PasswordGenerator:
    def __init__(self, start_unicode: int = 33, end_unicode: int = 127):
        """
        Initialize the password generator with the optional parameters.
        :param start_unicode: Start of the unicode range.
        :param end_unicode: End of the unicode range.
        """
        self.start_unicode = start_unicode
        self.end_unicode = end_unicode
        self.available_chars = self.get_all_characters_in_range()

    def get_all_characters_in_range(self) -> list[str]:
        """
        :return: List of characters in the range.
        """
        return [chr(character) for character in range(self.start_unicode, self.end_unicode + 1)]

    def generate_random_password(self, length: int = 8) -> str:
        """
        Generate a random password.
        :param length: Length of the password.
        :return: Random password.
        """
        password = ''.join([choice(self.available_chars) for _ in range(length)])
        return password


if __name__ == '__main__':
    quantity = int(input('How many passwords do you want? '))
    quality = int(input('How many characters you want in your password(s)? '))
    while quantity:
        print(PasswordGenerator().generate_random_password(int(quality)))
        quantity -= 1
