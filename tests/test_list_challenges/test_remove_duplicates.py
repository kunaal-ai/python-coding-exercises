import pytest
import list_challenges.remove_duplicates as rd


class TestRemoveDuplicates:
    @pytest.mark.parametrize(
        "test_input, expected_output",
        [
            ([1, 2, 3, 4, 1], [1, 2, 3, 4]),  # some duplicates
            ([1, 1, 1, 1], [1]),  # all duplicates
            ([1], [1]),  # single element
            ([1, 2, 3], [1, 2, 3]),  # no duplicates
            (
                [10, -1, 10, 20],
                [10, -1, 20],
            ),  # negative and positive integers
        ],
    )
    def test_remove_duplicates_in_list_positive(self, test_input, expected_output):
        """test for positive valid cases

        Args:
            test_input (_type_): list of int as input
            expected_output (_type_): list as output
        """
        response = rd.RemoveDuplicates(test_input)
        assert response.remove_duplicate_in_list() == expected_output

    def test_remove_duplicates_in_list_value_error(self):
        """test for value errors on empty input"""
        with pytest.raises(ValueError, match="Given list is empty"):
            response = rd.RemoveDuplicates([])
            response.remove_duplicate_in_list()

    @pytest.mark.parametrize(
        "test_input",
        [
            [1, 2, 3, "Test"],  # List containing a string
            [1, 2, None],  # List containing None
            [1.0, 2, 3],  # List containing a float
            "Not a list",  # Input is not a list
        ],
    )
    def test_remove_duplicate_in_list(self, test_input):
        """test using invalid types in list

        Args:
            test_input (list): list of various invalid data types
        """
        with pytest.raises(TypeError, match="Invalid Type"):
            response = rd.RemoveDuplicates(test_input)
            response.remove_duplicate_in_list()

    def test_remove_duplicates_init(self):
        """test_remove_duplicates_init covers the initialization process for
        different types of valid inputs."""
        response = rd.RemoveDuplicates([1, 2, 3])
        assert response.user_list == [1, 2, 3]

    def test_remove_duplicates_large_list(self):
        """test with large inputs"""
        large_input = list(range(1000)) + list(
            range(500)
        )  # 1000 unique + 500 duplicates
        expected_output = list(range(1000))
        response = rd.RemoveDuplicates(large_input)
        assert response.remove_duplicate_in_list() == expected_output
