"""
Error Operations Class
"""

class ErrorOperations:
    def __init__(self, array):
        self.array = array
        
    # error_equal_count checks if two characters have the same number of occurences
    def __error_equal_count(self, char1, char2,):
        count1 = 0
        count2 = 0
        # counts both characters
        for index in range(len(self.array)):
            if self.array[index] == char1:
                count1 += 1
            if self.array[index] == char2:
                count2 += 1
        # if counts are equal, return True
        if count1 == count2:
            return True
        # return False
        return False
    
    def __is_int(self, str_num):
        try:
            int(str_num.strip())
            return True
        except:
            return False        
    
    def __is_negative(self, str_num):
        if self.__is_int(str_num) and -1 * int(str_num) > 0:
            return True
        return False
    
    # error_operations determines whether a given array that forms a math expression has any invalid syntax
    # example: ["2", "+", "3"] is valid, but ["+", "2", "3"], ["(", ")", "2"] and ["1", "+", "+"] is not
    def error_operations(self):
        # initialize boolean variable
        error_bool = False
        # initialize variable for previous index
        prev_item = None
        
        # if brackets are not equal in count, it is error
        if not self.__error_equal_count('(', ')'):
            error_bool = True
            return error_bool
        
        for index, item in enumerate(self.array):
            # if two numbers are consecutive, then it is error
            if prev_item and self.__is_int(prev_item) and self.__is_int(item):
                error_bool = True
                break
            
            # if two symbols are consecutive, then it is error
            if prev_item and prev_item in '+-' and item in '+-':
                error_bool = True
                break
            
            # if start of array has + or -, then it is error
            if index == 0 and item in '+-':
                error_bool = True
                break
            
            # if end of array has + or -, then it is error
            if index == len(self.array) - 1 and item in '+-':
                error_bool = True
                break
            
            # if prev_item is int, item is (, it is error
            if prev_item and self.__is_int(prev_item) and item == '(':
                error_bool = True
                break
            
            # if prev_item = ), item is int, it is error
            if prev_item == ')' and self.__is_int(item):
                error_bool = True
                break
            
            # if prev and item are (, ) respectively, it is error
            if prev_item == '(' and item == ')':
                error_bool = True
                break
            
            # if no ( before for adding/subtracting negative numbers, it is error
            if self.__is_negative(item):
                if prev_item and prev_item in '+-':
                    error_bool = True
                    break

            
            # sets prev_item as item for next iteration
            prev_item = item
        
        # returns boolean
        return error_bool