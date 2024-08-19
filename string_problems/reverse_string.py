# Reverse a string without using any built-in functions or slicing.
class ReverseString:
    """A class to reverse a given string."""

    def __init__(self, g_string: str) -> None:
        """
        Initializes the ReverseString class with a string.

        Args:
            string (str): The string to be reversed.
        """
        self.g_string = g_string

    def string_sanitization(self, raw_value):
        """Sanitize the input values for invalid string inputs

        Args:
            raw_value (_type_): user given string value to sanitize

        Raises:
            TypeError: check if data type is not string
            ValueError: check if empty value given
        """
        if not isinstance(raw_value, str):
            raise TypeError("DataType not string")
        if raw_value == "":
            raise ValueError("Given string is empty")

    def reverse_the_string(self):
        """
        Reverses the stored string.

        Returns:
            final_string: The reversed string.
        """
        self.string_sanitization(self.g_string)
        final_string = ""
        for el in self.g_string:
            final_string = el + final_string

        return final_string


if __name__ == "__main__":
    obj = ReverseString("TestGuardian")
    response = obj.reverse_the_string()
    print(f"Reversed String is {response}")
