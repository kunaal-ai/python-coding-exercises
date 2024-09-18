# Create a function to check if two strings are anagrams of each other.

class AnagramWords:

    def __init__(self, left_string, right_string) -> None:
        self.left_string = left_string.lower().strip()
        self.right_string = right_string.lower().strip()

    def is_anagram(self) -> bool:
        return sorted(self.left_string) == sorted(self.right_string)


if __name__ == "__main__":
    obj = AnagramWords("SILENT", "listen")
    print(f"Given values are Anagram: {obj.is_anagram()}")