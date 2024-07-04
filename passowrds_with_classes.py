from random import choice


class PasswordGenerator:
    """
    Represents password generation functionality.
    It allows creating random passwords from a range of Unicode characters specified by the user.
    By default, the range includes characters from 33 to 127, which covers most printable ASCII characters
    """

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
        Generates a random password.
        :param length: Length of the password.
        :return: Random password.
        """
        password = ''.join([choice(self.available_chars) for _ in range(length)])
        return password

    def run(self) -> None:
        """
        Prompts the user for input to generate a specified number of passwords with specified length.
        Then prints the generated passwords one by one.
        """
        num_of_passwords = int(input('How many passwords do you want? '))
        len_of_passwords = int(input('How many characters you want in your password(s)? '))
        while num_of_passwords:
            print(password_generator.generate_random_password(len_of_passwords))
            num_of_passwords -= 1


if __name__ == '__main__':
    password_generator = PasswordGenerator()
    password_generator.run()
