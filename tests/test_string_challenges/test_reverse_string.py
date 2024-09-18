import pytest
import string_challenges.reverse_string as rs


class TestReverseString:
    """
    Test suite for the ReverseString class.

    This test class contains a parametrized test method to
    validate the functionality of ReverseString class.
    """

    @pytest.mark.parametrize(
        "test_input, expected_output",
        [
            ("TestGuardian", "naidrauGtseT"),
            ("123456", "654321"),
            ("a", "a"),
        ],
    )
    def test_reverse_the_string_positive(self, test_input, expected_output):
        """
        checks if the reverse_the_string method correctly reverses the input string.

        Args:
            test_input (str): The input string to be reversed.
            expected_output (str): The expected reversed string.

        Asserts:
            The reversed string matches the expected output.
        """
        response = rs.ReverseString(test_input)
        assert response.reverse_the_string() == expected_output

    @pytest.mark.parametrize(
        "test_input",
        [(""), (" ")],
    )
    def test_reverse_the_string_value_error(self, test_input):
        """Input Value Error
        Checks and raises on ValueError
        """
        with pytest.raises(ValueError, match="Given string is empty"):
            response = rs.ReverseString(test_input)
            response.reverse_the_string()

    @pytest.mark.parametrize(
        "test_input",
        [(1234), (0000), (-2233)],
    )
    def test_reverse_the_string_type_error(self, test_input):
        """Data Type Error
        Checks and raises on DataType Error
        """
        with pytest.raises(TypeError, match="DataType not string"):
            response = rs.ReverseString(test_input)
            response.reverse_the_string()
