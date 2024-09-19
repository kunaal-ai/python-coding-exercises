import pytest
import list_challenges.largest_number as ln


class TestLargestNumber:
    """Test the largest_number_is function
    """
    @pytest.mark.parametrize(
        "test_input, expected_output",
        [([1, 2, 3], 3), ([1, 1, 1, 1], 1), ([-5, 0, 5], 5)],
    )
    def test_largest_number_valid_inputs(self, test_input, expected_output):
        """test with expected valid inputs and outputs

        Args:
            test_input (list[int]): list of int
            expected_output (int): int
        """
        response = ln.LargestNumber(test_input)
        assert response.largest_number_is() == expected_output

    def test_largest_number_value_error_init(self):
        """raises Value error if empty list
        """
        with pytest.raises(ValueError, match="The given list is empty."):
            response = ln.LargestNumber([])
            response.largest_number_is()

    @pytest.mark.parametrize(
        "test_input", [([1, 2, None]), ([1, 2, "string"]), ([1, 2, 33.4]), "Not a list"]
    )
    def test_largest_numbers_type_error_init(self, test_input):
        """test __init__ to accept only int values list
        else raises TypeError

        Args:
            test_input (any): invalid values
        """
        with pytest.raises(TypeError, match="All elements must be int"):
            response = ln.LargestNumber(test_input)
            response.largest_number_is()

    
