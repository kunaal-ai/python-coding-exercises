import pytest
import string_problems.palindrome_string as ps


@pytest.mark.parametrize("test_input, expected_output", [
    ("civic", True),                  # Single-word palindrome
    ("hello", False),                 # Non-palindrome single word
    ("123hello321", False),           # Non-palindrome with numbers
    ("!@#Civic!@#", False),            # Palindrome with special characters
    ("", True),                       # Empty string
    ("a", True),                      # Single character
    ("12321", True),                  # Numeric palindrome
    ("12345", False)                  # Non-palindrome numeric string
])
class TestPalindrome:

    def test_is_palindrom(self, test_input, expected_output):
        response = ps.PalindromeString(test_input)
        assert response.is_palindrome() == expected_output
    
    def is_palindrome_optimized(self, test_input, expected_output):
        response = ps.PalindromeString(test_input)
        assert response.is_palindrome() == expected_output