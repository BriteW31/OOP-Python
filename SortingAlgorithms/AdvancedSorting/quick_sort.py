"""
QuickSort Algorithm
"""
class QuickSort:
    
    # Swap swaps the values of the two variables, number_one and number_two
    @staticmethod
    def swap(number_list, index_one, index_two):
        # define temporary variable to hold a value to complete swap
        temp = number_list[index_one]
        number_list[index_one] = number_list[index_two]
        number_list[index_two] = temp

    # Partition finds a value such that all elements less than it are left, greater than on right
    def partition(self, number_list, low, high):
        # define temporary pivot
        pivot = number_list[high]
        
        # initialize a counter
        count = low - 1
        
        # for loop to find a smaller value than the temporary pivot
        for index in range(low, high):
            if number_list[index] <= pivot:
                # increases count value if value is found
                count = count + 1
                
                # Swap the position of the count, and corresponding index
                QuickSort.swap(number_list, count, index)
                
        # swaps the count's position, with the high_index value
        QuickSort.swap(number_list, count + 1, high)
        
        # return counter
        return count + 1

    def quick_sort(self, number_list, low_index, high_index):
        if low_index < high_index:
            # define the pivot needed to order elements
            pivot = self.partition(number_list, low_index, high_index)
            
            # recursive call, where pivot is value, until the low is bigger than high
            self.quick_sort(number_list, low_index, pivot - 1)
            self.quick_sort(number_list, pivot + 1, high_index)
    
    def sort(self, array):
        size = len(array)
        self.quick_sort(array, 0, size - 1)

"""
# testing
test_array_1 = [20, 12, 15, 10, 11, 3, -6, 1, -10]
test_array_length = len(test_array_1)
QuickSort(test_array_1, 0, test_array_length - 1)
print(test_array_1)
"""