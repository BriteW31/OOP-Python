"""
Basic Sorting Class
"""
import bubble_sort as bubble
import selection_sort as select
import insertion_sort as insert
from file_reader import FileReader as reader

class BasicSorting:
    # Bubble Sort
    def bubble_sorter(self, array):
        print("Bubble Sort Start: ")
        bubble.bubble_sort(array, len(array))
        return array
    
    # Selection Sort
    def selection_sorter(self, array):
        print("Selection Sort Start: ")
        size = len(array)
        select.selection_sort(array, size)
        return array

    # Insertion Sort
    def insertion_sorter(self, array):
        print("Insertion Sort Start: ")
        size = len(array)
        
        # for loop to track indexes
        for index in range(1, size):
            
            # assume one value is already sorted
            temp = array[index]        
            steps = index - 1
            
            # while loop to organize all values greater than temp
            while steps >= 0 and temp < array[steps]:
                array[steps + 1] = array[steps]
                steps = steps - 1
                
            # set the element that is greater than temp the value of temp
            array[steps + 1] = temp
            
        return array

    # Print Product
    def printer(self, array):
        for i in range(len(array) - 1):
            print(array[i], end=", ")
        print(array[len(array) - 1]) 
    
    # Copy Data
    def copy_array(self, array):
        copy_array = []
        for index in range(len(array)):
            copy_array.append(array[index])
        return copy_array
    
        
if __name__ == "__main__":
    basic_sort = BasicSorting()
    data = reader().read_file("")
    print(data)
    
    bubble_sort_result = basic_sort.bubble_sorter(basic_sort.copy_array(data))
    print(bubble_sort_result)
    print("\n")
    print(data)
    
    selection_sort_result = basic_sort.selection_sorter(basic_sort.copy_array(data))
    print(selection_sort_result)
    print("\n")
    print(data)
    
    insertion_sort_result = basic_sort.insertion_sorter(basic_sort.copy_array(data))
    print(insertion_sort_result)
    print("\n")
    print(data)
    
    