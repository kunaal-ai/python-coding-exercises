# reverse a list without using inbuilt functions

class ReverseList:

    def __init__(self, given_list) -> None:
        self.given_list = given_list
        self._validate_inputs()

    def _validate_inputs(self) -> None:
        if not self.given_list:
            raise ValueError("given string is empty, expected a list")
        
        if any(not isinstance(i, int) for i in self.given_list):
            raise TypeError("Invalid value, expected int only")
    
    def reverse_a_list(self) -> list:
        list_reversed_order = []

        for i in range(len(self.given_list)-1, -1, -1):
            list_reversed_order.append(self.given_list[i])
        
        return list_reversed_order
    
    
if __name__ == "__main__":
    obj = ReverseList([1, 2, 3])
    print(obj.reverse_a_list())


