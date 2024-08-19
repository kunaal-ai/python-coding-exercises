# Create a function to check if a string is a palindrome.
class PalindromeString:
    """
    A class to check if a given string is a palindrome.
    """

    def __init__(self, given_string: str) -> None:
        """
        Initializes the PalindromeString with the given string.

        Args:
            given_string (str): The string to be checked.
        """

        self.given_string = given_string.strip()

    def is_palindrome(self) -> bool:
        """
        Checks if the given string is a palindrome.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """

        return self.given_string == self.given_string[::-1]


if __name__ == "__main__":
    obj = PalindromeString("121")
    response = obj.is_palindrome()
    print(f"Given value is : {response}")
