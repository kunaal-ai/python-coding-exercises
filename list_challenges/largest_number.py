# Find the largest number in a list without using inbuilt function.
class LargestNumber:
    """ if given list is not empty and all int values
    then find the largest number in given list and return    
    """
    def __init__(self, given_list) -> None:
        self.given_list = given_list
        self._validate_input()
    
    def _validate_input(self) -> None:
        """Validates that the input is a non-empty & list of integers."""
        if not self.given_list:
            raise ValueError("The given list is empty.")
        
        if not all(isinstance(i, int) for i in self.given_list):
            raise TypeError("All elements must be int")

    def largest_number_is(self):
        """ return the largest number in given list

        Returns:
            int: largest number in list
        """
        largest_number = 0
        for i in self.given_list:
            if i > largest_number:
                largest_number = i
        return largest_number 


if __name__ == "__main__":
    obj = LargestNumber([1, 1, 2, 5, 3, 4, 5, 7])
    print(obj.largest_number_is())
