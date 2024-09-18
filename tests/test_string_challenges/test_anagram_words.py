import pytest
import string_challenges.anagram_words as aw


class TestAnagramWords:
    @pytest.mark.parametrize("test_input_a, test_input_b, expected",
                             [
                                 ("listen", "silent", True),
                                 ("LISTEN", "silent", True),
                                 ("", "silent", False)
                             ],)
    def test_is_anagram(self, test_input_a, test_input_b, expected):
        """
        Test if two words are anagrams using parameterized inputs.

        Args:
            test_input_a (str): First word to compare.
            test_input_b (str): Second word to compare.
            expected (bool): Expected result if the words are anagrams.
        """
        response = aw.AnagramWords(test_input_a, test_input_b)
        assert response.is_anagram() == expected