# Write a program to count the number of vowels in a given string
class CountVowels:
    """Class gets a string value to find total vowels in it"""

    def __init__(self, given_string: str) -> None:
        self.given_string = given_string.strip()

    def count_total_vowels(self) -> int:
        """count total number of vowels in given string

        Raises:
            TypeError: if not a string
            ValueError: if empty string

        Returns:
            int: total number of vowels in the given string
        """
        if not isinstance(self.given_string, str):
            raise TypeError("DataType not string")
        if self.given_string == "":
            raise ValueError("Given string is empty")

        no_of_vowels = 0
        for i in self.given_string:
            if i.isalpha() and i in ["a", "e", "i", "o", "u"]:
                no_of_vowels += 1
        return no_of_vowels


obj = CountVowels("Test 9 Guardian")
RESPONSE = obj.count_total_vowels()
print(f"Total number of vowels : {RESPONSE}")
