import pytest
import string_problems.palindrome_string as ps
import string_problems.longest_word as lw
import string_problems.anagram_words as aw


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("121", True),
        ("Test", False),
    ],
)
class TestPalindromeString:

    def test_is_palindrome(self, test_input, expected):
        response = ps.PalindromeString(test_input)
        assert response.is_palindrome() is expected

    def test_is_palindrome_optimized(self, test_input, expected):
        response = ps.PalindromeString(test_input)
        assert response.is_palindrome_optimized() is expected


class TestLongestWord:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("This is the longest word in this string", "longest"),
            ("a", "a"),
        ],
    )
    def test_find_longest_word(self, test_input, expected):
        response = lw.LongestWord(test_input)
        assert response.find_longest_word() == expected


class TestAnagramWords:
    @pytest.mark.parametrize("test_input_a, test_input_b, expected",
                             [
                                 ("listen", "silent", True),
                                 ("LISTEN", "silent", True),
                                 ("", "silent", False)
                             ],)
    def test_is_anagram(self, test_input_a, test_input_b, expected):
        response = aw.AnagramWords(test_input_a, test_input_b)
        assert response.is_anagram() == expected