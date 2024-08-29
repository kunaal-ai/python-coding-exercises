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
        Option 01 - slow, if string is long

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """

        return self.given_string == self.given_string[::-1]
    
    def is_palindrome_optimized(self) -> bool:
        """ option 02 - optimized and fast

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """

        start = 0
        mid = len(self.given_string)//2
        tail = -1

        while start < mid:
            if self.given_string[start] == self.given_string[tail]:
                start += 1
                tail -= 1
            else:
                return False
        
        return True


if __name__ == "__main__":
    obj = PalindromeString("121")
    opt1_response = obj.is_palindrome()
    print(f"Given value is palindrome ? : {opt1_response}")

    opt2_response = obj.is_palindrome_optimized()
    print(f"Given value is palindrome ? Optimized way : {opt2_response}")
