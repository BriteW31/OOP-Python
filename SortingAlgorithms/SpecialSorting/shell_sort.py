"""
ShellSort Algorithm
"""

class ShellSort:
    @staticmethod
    def shell_sort(number_list, list_length):
        # define interval
        interval = list_length // 2
        
        # while loop to sort based on interval
        while interval > 0:
            
            # for loop to sort individual elements
            for index in range(interval, list_length):
                
                # define temp value, counter
                temp = number_list[index]
                count = index
                
                # move all elements down
                while count >= interval and number_list[count - interval] > temp:
                    number_list[count] = number_list[count - interval]
                    count -= interval
                    
                # sets the last element to temp
                number_list[count] = temp
                
            # decreases the interval
            interval = interval // 2
        
"""
# testing
test_array = [20, 12, 15, 10, 3, -6, 1, -10]
test_array_length = len(test_array)
ShellSort(test_array, test_array_length)
print(test_array)
"""