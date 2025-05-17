"""
HeapSort Algorithm
"""

class HeapSort:
    def __init__(self, array):
        self.array = array
    
    # Swap swaps the values of the two variables, number_one and number_two
    def __swap(self, index_one, index_two):
        # define temporary variable to hold a value to complete swap
        temp = self.array[index_one]
        self.array[index_one] = self.array[index_two]
        self.array[index_two] = temp
    
    # Heap obtains the binary tree of the array, then swaps positions
    def __heap(self, length, index):
        # define temporary maximum, left and right
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        # if largest can be replaced
        if left < length and self.array[index] < self.array[left]:
            largest = left
        if right < length and self.array[largest] < self.array[right]:
            largest = right
        
        # Swap and recursive call if largest is not located at root index
        if largest != index:
            self.__swap(index, largest)
            self.__heap(length, largest)
        
    def heap_sort(self, list_length):
        # build Heap
        for index in range(list_length // 2, -1, -1):
            self.__heap(list_length, index)
        
        # swap all elements
        for swap_index in range(list_length - 1, 0, -1):
            # Swap index with first element
            self.__swap(swap_index, 0)
            # Heap elements
            self.__heap(swap_index, 0)
        
        return self.array

"""
# testing
test_array = [20, 12, 15, 10, 3, -6, 1, -10]
test_array_length = len(test_array)
HeapSort(test_array, test_array_length)
print(test_array)
"""