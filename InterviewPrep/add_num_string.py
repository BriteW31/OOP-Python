"""
Add numbers from string
"""

class AddNumString:
    def __init__(self, string):
        self.string = string
    
    def __is_integer(self, input):
        try:
            int(input.lstrip().rstrip())
            return True
        except:
            return False
        
    def add_num_string(self):
        # modify string into string array
        modified_string = self.string.replace("(","").replace(")","").replace(" ","")
        string_array = modified_string.split("+")
        # define output as the sum of all numbers
        output = 0
        # check if every number as string is an integer
        for num_string in string_array:
            if self.__is_integer(num_string):
                # turns the string into int, then add int to output
                num_int = int(num_string.strip())
                output = output + num_int
        # returns output
        return output

# testing
test_string = " -2 + (-10 + 19) + (1 + -2 + (-3 )) +    4+3  +5 "
sum_string = AddNumString(test_string)
output_sum = sum_string.add_num_string()
print(output_sum)