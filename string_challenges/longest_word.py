# Write a Python program to find the longest word in a given string.
class LongestWord:

    def __init__(self, given_string: str) -> None:
        self.given_string = given_string
        self.list_of_given_string = self.given_string.split(" ")

    def find_longest_word(self) -> str:
        """
        Finds and returns the longest word in the list of strings.

        Iterates through the list of strings and compares the lengths of 
        the words to find the one with the maximum length.

        Returns:
            str: The longest word from the list of given strings.
            If multiple words have the same length, the first one encountered is returned.
        """   
        count = 0
        longest_word = ""
        for i in self.list_of_given_string:
            if len(i) > count:
                count = len(i)
                longest_word = i
        return longest_word


if __name__ == "__main__":
    obj = LongestWord("Find longest in this string")
    response = obj.find_longest_word()
    print(f"Longest word is :{response} ")
