import pytest
import string_challenges.palindrome_string as ps


class TestPalindrome:
    @pytest.mark.parametrize("test_input, expected_output", [
        ("civic", True),                  # Single-word palindrome
        ("", True),                       # Empty string
        ("a", True),                      # Single character
        ("12321", True),                  # Numeric palindrome
    ])
    def test_is_palindrom_expected_true(self, test_input, expected_output):
        """ Test is_palindrome for TRUE values only

        Args:
            test_input (_type_): value to be tested
            expected_output (_type_): expected respnse from function
        """        
        response = ps.PalindromeString(test_input)
        assert response.is_palindrome() == expected_output
    
    @pytest.mark.parametrize("test_input, expected_output", [
        ("hello", False),                 # Non-palindrome single word
        ("123hello321", False),           # Non-palindrome with numbers
        ("!@#Civic!@#", False),            # Palindrome with special characters
        ("12345", False)                  # Non-palindrome numeric string
    ])
    def test_is_palindrom_expected_false(self, test_input, expected_output):
        """ Test is_palindrome for FALSE values only

        Args:
            test_input (_type_): value to be tested
            expected_output (_type_): expected respnse from function
        """  
        response = ps.PalindromeString(test_input)
        assert response.is_palindrome() == expected_output