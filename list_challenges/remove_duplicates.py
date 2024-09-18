class RemoveDuplicates:
    """
    A class to remove duplicates from a list without using built-in functions.
    """

    def __init__(self, given_list: list) -> None:
        """
        Initialize with the provided list.
        
        Args:
            given_list (list): List to process.
        """
        self.user_list = given_list
    
    def remove_duplicate_in_list(self) -> list:
        """
        Remove duplicates from the list, preserving the order.

        Returns:
            list: List with duplicates removed.
        """
        len_user_list = len(self.user_list)
        if len_user_list == 0:
            raise ValueError("Given list is empty")
        
        for i in self.user_list:
            if not isinstance(i, int):
                raise TypeError("Invalid Type")
        
        if len_user_list == 1:
            return self.user_list
        
        unique_elements_list = []
        for i in self.user_list:
            if i not in unique_elements_list:
                unique_elements_list.append(i)
        return unique_elements_list


if __name__ == "__main__":
    obj = RemoveDuplicates([1, 2, 3, 1, 2])
    print(obj.remove_duplicate_in_list())
