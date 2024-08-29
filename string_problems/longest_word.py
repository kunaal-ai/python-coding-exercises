# Write a Python program to find the longest word in a given string.
class LongestWord:

    def __init__(self, given_string: str) -> None:
        self.given_string = given_string
        self.list_of_given_string = self.given_string.split(" ")

    def find_longest_word(self) -> str:
        count = 0
        longest_word = ""
        for i in self.list_of_given_string:
            if len(i) > count:
                count = len(i)
                longest_word = i
        return longest_word


obj = LongestWord("Find longest in this string")
response = obj.find_longest_word()
print(f"Longest word is :{response} ")
