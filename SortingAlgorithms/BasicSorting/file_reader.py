"""
File Reading Class
"""

# default
DEFAULT_PATH = "number.txt"

class FileReader:
            
    def __init__(self):
        self.output_array = []   
    
    # def private is_empty_string, checks if input is Null or empty
    def __is_empty_string(self, input):
        if input == None:
            return True
        if len(input) == 0:
            return True
        else:
            return False
    
    # define private is_number, checks if input is an integer
    def __is_number(self, input):
        try:
            int(input.lstrip().rstrip())
            return True
        except:
            return False
    
    # reads file, converts to array of integers
    def read_file(self, path: str):
        if self.__is_empty_string(path):
            path = DEFAULT_PATH
        with open(path, "r") as txt_file:
            input_data = [line.rstrip("\n") for line in txt_file]

            for item in input_data:
                temp_array = item.split(",")
                for numbers in temp_array:
                    if self.__is_number(numbers):
                        self.output_array.append(int(numbers))
            
            return self.output_array
        

