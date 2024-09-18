import pytest
import string_challenges.longest_word as lw


class TestLongestWord:
    """
    Test the LongestWord class from string_problems.longest_word.
    
    check the `find_longest_word` method with various inputs.
    """

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("This is the longest word in this string", "longest"),
            ("a", "a"),
        ],
    )
    def test_find_longest_word(self, test_input, expected):
        """
        Tests the find_longest_word method.

        Parameters:
        - test_input: Input string.
        - expected: Expected longest word.
        """
        response = lw.LongestWord(test_input)
        assert response.find_longest_word() == expected
