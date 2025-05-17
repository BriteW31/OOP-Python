"""
RadixSort Algorithm
"""

class RadixSort:
    def __init__(self, array):
        self.array = array
        
    # use counting sort to sort the elements in the basis of significant places
    def __counting_sort_alt(self, place):
        size = len(self.array)
        output = [0] * size
        count = [0] * 10
    
        # calculate count of elements
        for index_1 in range(0, size):
            index = self.array[index_1] // place
            count[index % 10] += 1
    
        # calculate cumulative count
        for index_2 in range(1, 10):
            count[index_2] += count[index_2 - 1]
    
        # place the elements in sorted order
        index_3 = size - 1
        while index_3 >= 0:
            index = self.array[index_3] // place
            output[count[index % 10] - 1] = self.array[index_3]
            count[index % 10] -= 1
            index_3 -= 1
            
        # copies output into array
        for index_4 in range(0, size):
            self.array[index_4] = output[index_4]
        
    
    def radix_sort(self):
        # get maximum element
        max_element = max(self.array)
    
        # counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            self.__counting_sort_alt(place)
            place *= 10
        
        return self.array

"""
# testing
test_array_1 = [121, 432, 564, 23, 1, 45, 788]
RadixSort(test_array_1)
print(test_array_1)

# negative numbers do not work
test_array_2 = [20, 12, 15, 10, 11, 3, -6, 1, -10]
RadixSort(test_array_2)
print(test_array_2)

test_array_2_positive = [20, 12, 15, 10, 11, 3, 6, 1, 10]
RadixSort(test_array_2_positive)
print(test_array_2_positive)
"""