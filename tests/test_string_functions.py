from typing import Literal
import pytest
import string_problems.reverse_string as rs
import string_problems.palindrome_string as ps


class TestReverseString:
    """
    Test suite for the ReverseString class.

    This test class contains a parametrized test method to
    validate the functionality of ReverseString class.
    """

    @pytest.mark.parametrize(
        "test_input, expected_output",
        [("TestGuardian", "naidrauGtseT"), ("123456", "654321"), ("a", "a")],
    )
    def test_reverse_the_string_parametrized(self, test_input, expected_output):
        """
        Test the reverse_the_string method with multiple input-output pairs.

        Using pytest's parametrize decorator to run the test with
        different sets of input and expected output values. It checks if the
        reverse_the_string method correctly reverses the input string.

        Args:
            test_input (str): The input string to be reversed.
            expected_output (str): The expected reversed string.

        Asserts:
            The reversed string matches the expected output.
        """
        response = rs.ReverseString(test_input)
        assert response.reverse_the_string() == expected_output

    def test_reverse_the_string_value_error(self):
        """Input Value Error
        Checks and raises on ValueError
        """
        with pytest.raises(ValueError, match="Given string is empty"):
            response = rs.ReverseString("")
            response.reverse_the_string()

    def test_reverse_the_string_type_error(self):
        """Data Type Error
        Checks and raises on DataType Error
        """
        with pytest.raises(TypeError, match="DataType not string"):
            response = rs.ReverseString(123456)
            response.reverse_the_string()


class TestPalindromeString:

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("121", True),
            ("Test", False),
        ],
    )
    def test_is_palindrome(self, test_input, expected):
        response = ps.PalindromeString(test_input)
        assert response.is_palindrome() is expected
